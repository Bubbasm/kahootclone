# Populate database
# This file has to be placed within the
# catalog/management/commands directory in your project.
# If that directory doesn't exist, create it.
# The name of the script is the name of the custom command,
# that is, populate.py.
#
# execute python manage.py  populate
#
# use module Faker generator to generate data
# (https://zetcode.com/python/faker/)
import os

from django.core.management.base import BaseCommand
from models.models import User as User
from models.models import Questionnaire as Questionnaire
from models.models import Question as Question
from models.models import Answer as Answer
from models.models import Game as Game
from models.models import Participant as Participant
from models.models import Guess as Guess

from faker import Faker


# The name of this class is not optional must be Command
# otherwise manage.py will not process it properly
class Command(BaseCommand):
    # helps and arguments shown when command python manage.py help populate
    # is executed.
    help = """populate kahootclone database
           """
    # if you want to pass an argument to the function
    # uncomment this line
    # def add_arguments(self, parser):
    #    parser.add_argument('publicId',
    #        type=int,
    #        help='game the participants will join to')
    #    parser.add_argument('sleep',
    #        type=float,
    #        default=2.,
    #        help='wait this seconds until inserting next participant')

    def __init__(self, sneaky=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # "if 'RENDER'" allows you to deal with different
        # behaviour in render.com and locally
        # That is, we check a variable ('RENDER')
        # that is only defined in render.com
        if 'RENDER' in os.environ:
            pass
        else:
            pass

        self.NUMBERUSERS = 4
        self.NUMBERQESTIONARIES = 30
        self.NUMBERQUESTIONS = 100
        self.NUMBERPARTICIPANTS = 20
        self.NUMBERANSWERPERQUESTION = 4
        self.NUMBERGAMES = 4

    # handle is another compulsory name, do not change it"
    # handle function will be executed by 'manage populate'
    def handle(self, *args, **kwargs):
        "this function will be executed by default"

        self.cleanDataBase()   # clean database
        # The faker.Faker() creates and initializes a faker generator,
        self.faker = Faker()
        self.user()  # create users
        self.questionnaire()  # create questionaries
        self.question()  # create questions
        self.answer()  # create answers
        self.game()  # create games
        # self.participant()  # create participants

    def cleanDataBase(self):
        # delete all models stored (clean table)
        # in database
        # order in which data is deleted is important

        Participant.objects.all().delete()
        Guess.objects.all().delete()
        Game.objects.all().delete()
        Answer.objects.all().delete()
        Question.objects.all().delete()
        Questionnaire.objects.all().delete()
        User.objects.all().delete()
        print("clean Database")

    def user(self):
        " Insert users"
        # create user
        print("Users")
        for _ in range(self.NUMBERUSERS):
            user = User()
            user.username = self.faker.name()
            user.set_password(self.faker.password())
            user.save()

    def questionnaire(self):
        "insert questionnaires"
        print("questionnaire")
        # assign users randomly to the questionnaires
        for _ in range(self.NUMBERQESTIONARIES):
            questionnaire = Questionnaire()
            questionnaire.title = self.faker.sentence()
            questionnaire.user = User.objects.order_by('?').first()
            questionnaire.save()

    def question(self):
        " insert questions, assign randomly to questionnaires"
        print("Question")
        # assign questions randomly to the questionnaires
        for _ in range(self.NUMBERQUESTIONS):
            question = Question()
            question.question = self.faker.sentence()[0:-1] + "?"
            question.questionnaire = Questionnaire.objects.order_by(
                '?').first()
            question.answerTime = self.faker.random_int(min=10, max=60)
            question.save()

    def answer(self):
        "insert answers, one of them must be the correct one"
        print("Answer")
        # assign answer randomly to the questions
        # maximum number of answers per question is four
        for q in Question.objects.all():
            for n in range(self.NUMBERANSWERPERQUESTION):
                answer = Answer()
                answer.answer = self.faker.word()
                answer.question = q
                answer.correct = n == 0
                answer.save()

    def game(self):
        "insert some games"
        print("Game")
        # choose at random the questionnaries
        for _ in range(self.NUMBERGAMES):
            game = Game()
            game.questionnaire = Questionnaire.objects.order_by('?').first()
            game.countdownTime = self.faker.random_int(min=5, max=10)
            game.save()

    def participant(self):
        "insert participants"
        print("Participant")
        # choose at random the games
        for _ in range(self.NUMBERPARTICIPANTS):
            participant = Participant()
            participant.alias = self.faker.name()
            participant.game = Game.objects.order_by('?').first()
            participant.save()
