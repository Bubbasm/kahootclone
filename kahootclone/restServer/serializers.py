from models.models import Participant, Game, Guess, Question
from rest_framework import serializers


class ParticipantSerializer(serializers.ModelSerializer):
    '''
    Serializer para el modelo de participante.
    '''
    class Meta:
        model = Participant
        fields = ('alias', 'points', 'uuidP')

    def create(self, validated_data):
        '''
        Por robustez de la API, se retornan únicamente los campos necesarios.
        En este caso, obviamos el id de la base de datos del participante y
        el id del juego asociado.
        @author: Bhavuk Sikka
        '''
        gamepk = self.context['request'].data['game']
        game = Game.objects.get(pk=gamepk)
        participant = Participant.objects.create(game=game, **validated_data)
        return participant


class GameSerializer(serializers.ModelSerializer):
    '''
    Serializer para el modelo de juego.
    '''
    answerCount = serializers.SerializerMethodField()

    def get_answerCount(self, game: Game):
        '''
        Método para obtener el número de respuestas de la pregunta actual.
        @author: Bhavuk Sikka
        '''
        q_list = list(Question.objects.filter(
            questionnaire=game.questionnaire))
        if game.questionNo >= len(q_list):
            return 0
        return q_list[game.questionNo].answer_set.all().count()

    class Meta:
        model = Game
        fields = ('state', 'publicId', 'questionNo', 'answerCount')


class GuessSerializer(serializers.ModelSerializer):
    '''
    Serializer para el modelo de guess.
    '''
    class Meta:
        model = Guess
        fields = ()

    def create(self, validated_data):
        '''
        Por robustez de la API, se retornan únicamente los campos necesarios.
        En este caso no hace falta ningún campo, sino solo saber que el guess
        se ha creado correctamente.
        @author: Bhavuk Sikka
        '''
        game = self.context['request'].data['game']
        participant = self.context['request'].data['participant']
        question = self.context['request'].data['question']
        answer = self.context['request'].data['answer']

        return Guess.objects.create(game=game,
                                    participant=participant,
                                    question=question,
                                    answer=answer)
