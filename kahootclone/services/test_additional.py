from time import sleep
from django.urls import reverse
from models.models import Answer, Game, Participant, User
from services.test_services_game import GAME_QUESTION_SERVICE, \
    GAME_UPDATE_PARTICIPANT_SERVICE
from services.test_services import ANSWER_CREATE_SERVICE, ANSWER_UPDATE_SERVICE
from services.test_services import GAME_CREATE_SERVICE
from services.test_services import ServiceTests


class AdditionalTest(ServiceTests):
    '''
    Tests for 100% coverage.
    '''

    def test002_testAnswerCreateAndUpdateView(self):
        '''
        Test that the AnswerCreateView is working correctly.
        @author: Samuel de Lucas
        '''
        # create answer with correct=True,
        # when there is already one with correct=True
        args = [str(self.question.id)]
        kwargs = {'answer': 'test', 'correct': True}
        self.checkLogin(ANSWER_CREATE_SERVICE, 'DO_NOT_CHECK_KEY', args=args)
        response = self.checkLoginSecondPart(
            ANSWER_CREATE_SERVICE, args, kwargs)
        self.assertNotEqual(
            self.decode(
                response.content).find(
                    "There is already a correct answer defined"), -1)

        # create two more answers so that there are already 4
        answerDict3 = self.answerDict2.copy()
        answerDict3['answer'] = 'test3'
        Answer.objects.get_or_create(**answerDict3)[0]

        answerDict4 = self.answerDict2.copy()
        answerDict4['answer'] = 'test4'
        Answer.objects.get_or_create(**answerDict4)[0]

        # create a fifth answer (not allowed)
        kwargs = {'answer': 'test', 'correct': False}
        self.checkLogin(ANSWER_CREATE_SERVICE, 'DO_NOT_CHECK_KEY', args=args)
        response = self.checkLoginSecondPart(
            ANSWER_CREATE_SERVICE, args, kwargs)
        self.assertNotEqual(
            self.decode(
                response.content).find(
                    "There can only be a maximum of 4 answers"), -1)

        # update answer with correct=True,
        # when there is already one with correct=True
        args = [str(self.answer2.id)]
        kwargs = self.answerDict2.copy()
        kwargs['correct'] = True
        self.checkLogin(ANSWER_UPDATE_SERVICE, 'DO_NOT_CHECK_KEY', args=args)
        response = self.checkLoginSecondPart(
            ANSWER_UPDATE_SERVICE, args, kwargs)
        self.assertNotEqual(
            self.decode(
                response.content).find(
                    "There is already a correct answer defined"), -1)

    def test004_testGameUpdateParticipant(self):
        '''
        This test is equal to the last part of test01_gameUpdateParticipant,
        but it adds the publicId to the request, necessary to test the view
        completely and get 100% coverage
        @author: Samuel de Lucas
        '''

        # create game
        game = Game.objects.get_or_create(questionnaire=self.questionnaire)[0]

        # create new user, it will be used for login
        # and will not be the owner of the questionnaire
        self.userDict = {"username": 'b',
                         "password": 'b',
                         "first_name": 'b',
                         "last_name": 'b',
                         "email": 'b@bb.es'}
        user, created = User.objects.get_or_create(**self.userDict)
        if created:
            user.set_password(self.userDict['password'])
            user.save()
        self.user = user
        args = [str(self.questionnaire.id)]
        self.checkLogin(GAME_CREATE_SERVICE, 'DO_NOT_CHECK_KEY', args=args)
        response = self.client1.get(
            reverse(GAME_UPDATE_PARTICIPANT_SERVICE) +
            str(game.publicId), follow=True)

        self.assertNotEqual(
            self.decode(
                response.content).find("does not belong to logged user"), -1)

    def test_005_testInvalidSessionGameCountdown(self):
        '''
        Test behaviour when publicId is not correctly set
        in the session in gameCountdownView.
        @author: Samuel de Lucas
        '''
        # request gameCountdownView without publicId in session
        self.checkLogin('game-count-down',
                        'DO_NOT_CHECK_KEY')
        response = self.client1.get(
            reverse('game-count-down'), follow=True)
        self.assertNotEqual(
            self.decode(
                response.content).find("403 Forbidden"), -1)

    def test_006_testCountDown2(self):
        """
        Check how the estate of game changes as we play.
        This test is very dependent on implementation, fill free to change it
        """
        from models.constants import WAITING

        self.question.answerTime = 2
        self.question.save()
        self.question2.answerTime = 2
        self.question2.save()

        # create game
        id = self.questionnaire.id
        args = [str(id)]
        response = self.checkLogin(
            GAME_CREATE_SERVICE, 'DO_NOT_CHECK_KEY', args=args)
        game = Game.objects.first()
        self.assertEqual(game.state, WAITING)
        self.assertNotEqual(
            self.decode(
                response.content).find("Game - Kahoot clone"), -1)

        # join game
        Participant.objects.create(game=game, alias="alias_1")

        # check game state when accesing through GAME_QUESTION_SERVICE
        # (should be waiting)
        response = self.client1.get(
            reverse(GAME_QUESTION_SERVICE), follow=True)
        self.assertNotEqual(
            self.decode(
                response.content).find("Waiting - Kahoot clone"), -1)

        # start game (simulate clicking the button)
        response = self.client1.post(reverse('game-count-down'), follow=True,
                                     data={'launch': True})

        # wait for countdown
        sleepTime = game.countdownTime
        print("waiting for game to start (" + str(sleepTime) + " seconds)")
        sleep(sleepTime)

        # get page after countdown (should not be changed, as a post is needed)
        response = self.client1.get(
            reverse(GAME_QUESTION_SERVICE), follow=False)
