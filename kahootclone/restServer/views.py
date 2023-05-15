from models.models import Answer, Participant, Game, Guess, Question
from models.constants import QUESTION, WAITING
from .serializers import ParticipantSerializer, GameSerializer, GuessSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from faker import Faker
from faker.providers.person.es_ES import Provider

fake = Faker()
fake.add_provider(Provider)

errorResponse = {
    'error': 'Authentication credentials were not provided.'
}

gameNotExist = "Game does not exist"
aliasInUse = "Alias already in use"
gameStarted = "Game already started"
participantNotExist = "Participant does not exist"
questionFinished = "Wait until the question is shown"
guessExists = "Guess already exists"
answerNotExist = "Answer does not exist"

# nombres graciosos en español
nameCollection = [
    'ElvisTek',
]


class GameViewSet(viewsets.ModelViewSet):
    '''
    ViewSet for Game model
    '''
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = 'publicId'


class ParticipantViewSet(viewsets.ModelViewSet):
    '''
    ViewSet for Participant model
    '''
    queryset = Participant.objects.values('alias', 'points', 'uuidP')
    serializer_class = ParticipantSerializer
    permission_classes = [AllowAny]

    def getUnrepeatedAlias(self, game) -> str:
        participants = Participant.objects.filter(game=game)
        aliasesUsed = [p.alias for p in participants]
        aliasRemainder = [p for p in nameCollection if p not in aliasesUsed]
        if len(aliasRemainder) > 0:
            return aliasRemainder[0]
        tries = 0
        while tries < 500:
            alias = fake.first_name()
            if alias not in aliasesUsed:
                return alias
            tries += 1
        return "Jugador"

    def create(self, request, *args, **kwargs):
        '''
        Create a new participant for the game
        Checks if the alias is already in use
        @author: Samuel de Lucas
        '''
        if hasattr(request.data, '_mutable'):
            request.data._mutable = True
        gameID = request.data['game']
        try:
            game = Game.objects.get(publicId=gameID)
        except Game.DoesNotExist:
            return Response({'error': gameNotExist}, status=404)

        try:
            alias = request.data['alias']
        except Exception:
            alias = self.getUnrepeatedAlias(game)
            request.data['alias'] = alias

        request.data['game'] = game.id
        if Participant.objects.filter(game__publicId=gameID,
                                      alias=alias).exists():
            return Response({'error': aliasInUse}, status=403)
        if game.state != WAITING:
            return Response({'error': gameStarted}, status=403)

        return super(ParticipantViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        '''
        Prevent deleting participants
        @author: Samuel de Lucas
        '''
        return Response(errorResponse, status=403)

    def update(self, request, *args, **kwargs):
        '''
        Prevent updating participants
        @author: Samuel de Lucas
        '''
        return Response(errorResponse, status=403)

    def retrieve(self, request, *args, **kwargs):
        '''
        Prevent retrieving participants
        @author: Samuel de Lucas
        '''
        return Response(errorResponse, status=403)

    def list(self, request):
        '''
        Prevent listing all participants
        @author: Samuel de Lucas
        '''
        return Response(errorResponse, status=403)


class GuessViewSet(viewsets.ModelViewSet):
    '''
    ViewSet for Guess model
    '''
    queryset = Guess.objects.all().values('participant', 'answer')
    serializer_class = GuessSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        '''
        Create a new guess for the game
        El metodo admite la creaci ́on de un unico guess por cada tupla
        (participante, pregunta), igualmente comprueba antes de añadir el
        guess que el participante existe y el estado del juego (game.state)
        es QUESTION.
        @author: Bhavuk Sikka
        '''

        participantUid = request.data['uuidp']
        gameId = request.data['game']
        if not Participant.objects.filter(uuidP=participantUid).exists():
            return Response({'error': participantNotExist},
                            status=403)
        game = Game.objects.get(publicId=gameId)
        request.data['game'] = game
        questionNo = game.questionNo
        questionnaire = game.questionnaire
        question = Question.objects.filter(
            questionnaire=questionnaire).all()[questionNo]
        request.data['question'] = question
        answerIndex = request.data['answer']
        try:
            answer = Answer.objects.filter(
                question=question).all()[answerIndex]
        except IndexError:
            return Response({'error': answerNotExist},
                            status=403)
        request.data['answer'] = answer
        if game.state != QUESTION:
            return Response({'error': questionFinished},
                            status=403)
        participant = Participant.objects.get(uuidP=participantUid)
        request.data['participant'] = participant
        if Guess.objects.filter(participant=participant,
                                question=question).exists():
            return Response({'error': guessExists},
                            status=403)
        return super(GuessViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        '''
        Prevent retreiving guesses
        @Samuel de Lucas
        '''
        return Response(errorResponse, status=403)

    def destroy(self, request, *args, **kwargs):
        '''
        Prevent deleting guesses
        @Samuel de Lucas
        '''
        return Response(errorResponse, status=403)

    def update(self, request, *args, **kwargs):
        '''
        Prevent updating guesses
        @Samuel de Lucas
        '''
        return Response(errorResponse, status=403)

    def list(self, request):
        '''
        Prevent listing all guesses
        @Samuel de Lucas
        '''
        return Response(errorResponse, status=403)
