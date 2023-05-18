from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.urls import reverse
from random import randint
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid
from models.constants import WAITING


class User(AbstractUser):
    '''
    Default user class, just in case we want
    to add something extra in the future
    '''
    objects = UserManager()


class Questionnaire(models.Model):
    '''Model representing a questionnaire.'''
    title = models.CharField(
        max_length=200, help_text='Enter the title of the questionnaire')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        String for representing the Model object.
        @author: Samuel de Lucas
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the URL to access a detail record for this questionnaire.
        @author: Samuel de Lucas
        """
        return reverse('questionnaire-detail', args=[str(self.id)])

    class Meta:
        '''
        Class that defines the order in which the questionnaires will be shown
        '''
        ordering = ['-created_at']


class Question(models.Model):
    '''Model representing a question.'''
    question = models.CharField(max_length=200, help_text='Enter the question')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    answerTime = models.IntegerField(default=30, blank=True)

    def __str__(self):
        """
        String for representing the Model object.
        @author: Samuel de Lucas
        """
        return self.question

    class Meta:
        '''
        Class that defines the order in which the questions will be shown.
        '''
        ordering = ['created_at']


class Answer(models.Model):
    '''Model representing an answer.'''
    answer = models.CharField(max_length=200, help_text='Enter the answer')
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        """
        String for representing the Model object.
        @author: Bhavuk Sikka
        """
        return str(self.question) + " - " + self.answer

    class Meta:
        '''
        Class that defines the order in which the questions will be shown.
        '''
        ordering = ['id']


class Game(models.Model):
    '''Model representing a game.'''
    created_at = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(
        default=WAITING,
        validators=[MinValueValidator(1), MaxValueValidator(4)]
    )
    publicId = models.IntegerField(
        default=0, unique=True
    )
    countdownTime = models.IntegerField(
        default=5
    )
    questionNo = models.IntegerField(default=0)
    questionnaire = models.ForeignKey(
        Questionnaire,
        on_delete=models.CASCADE
    )
    lastTimeButtonPressed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String for representing the Model object.
        @author: Bhavuk Sikka
        """
        return str(self.questionnaire) + " - " + \
            str(self.publicId) + " - " + str(self.state)

    def save(self, *args, **kwargs):
        '''
        If the game is created, it will be assigned a random publicId.
        @author: Bhavuk Sikka
        '''
        if self.publicId == 0:
            self.publicId = randint(1, 1000)
        super(Game, self).save()

    class ChangeState(Exception):
        '''
        Exception that indicates the game state must change
        Used in GameCountdownView
        '''
        pass


class Participant(models.Model):
    '''Model representing a participant.'''
    alias = models.CharField(max_length=20,
                             help_text='Enter the alias of the participant')
    points = models.IntegerField(default=0)
    uuidP = models.UUIDField(default=uuid.uuid4, editable=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        """
        String for representing the Model object.
        @author: Samuel de Lucas
        """
        return self.alias + " (" + str(self.points) + " points)"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['alias', 'game'],
                                    name='Participant of game')
        ]


class Guess(models.Model):
    '''Model representing a guess.'''
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        """
        String for representing the Model object.
        @author: Bhavuk Sikka
        """
        return str(self.participant) + " - " +\
            str(self.question) + " - " + str(self.answer)

    def save(self, *args, **kwargs):
        '''
        If the answer is correct, the participant gets a point.
        @author: Bhavuk Sikka
        '''
        if self.answer.correct:
            self.participant.points += 1
            self.participant.save()

        super(Guess, self).save()
