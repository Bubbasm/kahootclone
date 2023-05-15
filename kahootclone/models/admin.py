from django.contrib import admin
from .models import User, Questionnaire, Question, Answer
from .models import Game, Participant, Guess

admin.site.register(User)
admin.site.register(Questionnaire)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Game)
admin.site.register(Participant)
admin.site.register(Guess)
