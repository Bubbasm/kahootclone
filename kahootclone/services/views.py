from datetime import timedelta, datetime, timezone
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.core import serializers

from models.models import Questionnaire, Question
from models.models import Answer, Game, Participant
from models.constants import WAITING, QUESTION, ANSWER, LEADERBOARD

from kahootclone.settings import GAME_JOIN_URL


class HomeView(generic.TemplateView):
    '''Home page view'''
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        '''
        Get context. Includes user's latest 5
        questionnaires if it is authenticated
        @author: Bhavuk Sikka
        '''
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['latest_questionnaire_list'] = Questionnaire.objects.\
                filter(user=self.request.user).order_by('-created_at')[:5]
        return context


class QuestionnaireListView(LoginRequiredMixin, generic.ListView):
    '''
    List of questionnaires view.
    Only shows the questionnaires of the logged in user
    '''
    model = Questionnaire
    paginate_by = 10

    def get_queryset(self):
        '''
        Get queryset. Returns the questionnaires of the logged in user,
        and the questions associated to each questionnaire.
        @author: Samuel de Lucas
        '''
        questionnaires = Questionnaire.objects.filter(user=self.request.user)
        for questionnaire in questionnaires:
            questionnaire.questions = questionnaire.question_set.all()
        return questionnaires


class QuestionnaireDetailView (LoginRequiredMixin,
                               UserPassesTestMixin,
                               generic.DetailView):
    '''
    Detail of a questionnaire view.
    Shows questions of the corresponding questionnaire
    '''
    model = Questionnaire

    def get_context_data(self, **kwargs):
        '''
        Get context. Includes the questions of the questionnaire and
        the answers of each question.
        @author: Bhavuk Sikka
        '''
        context = super().get_context_data(**kwargs)
        context['question_list'] = self.object.question_set.all()
        for question in context['question_list']:
            question.answers = Answer.objects.filter(question=question)

        return context

    def test_func(self):
        '''
        Test function. Checks if the logged in user is the owner of
        the questionnaire.
        Avoids users to see questionnaires that are not theirs.
        @author: Samuel de Lucas
        '''
        return self.get_object().user == self.request.user


class QuestionnaireRemoveView (LoginRequiredMixin,
                               UserPassesTestMixin,
                               DeleteView):
    '''View to remove a questionnaire'''
    model = Questionnaire
    success_url = reverse_lazy('questionnaire-list')

    def test_func(self):
        '''
        Test function. Checks if the logged in user is the owner
        of the questionnaire.
        Avoids users to delete questionnaires that are not theirs.
        @author: Samuel de Lucas
        '''
        return self.get_object().user == self.request.user


class QuestionnaireUpdateView(LoginRequiredMixin,
                              UserPassesTestMixin,
                              UpdateView):
    '''View to update a questionnaire. Only includes the title field.'''
    model = Questionnaire
    fields = ['title']

    def get_context_data(self, **kwargs):
        '''
        Get context. Includes the question of the answer.
        Sets the isUpdate variable to True to show the correct template.
        @author: Bhavuk Sikka
        '''
        context = super().get_context_data(**kwargs)
        context['isUpdate'] = True
        return context

    def form_valid(self, form):
        '''
        Checks that the form is valid.
        Sets the user of the questionnaire to the logged in user.
        @author: Bhavuk Sikka
        '''
        form.instance.user = self.request.user
        return super(QuestionnaireUpdateView, self).form_valid(form)

    def get_success_url(self) -> str:
        '''
        Returns the url to redirect after the update is successful.
        Redirects to the questionnaire detail view of the updated
        questionnaire.
        @author: Bhavuk Sikka
        '''
        return reverse('questionnaire-detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        '''
        Test function. Checks if the logged in user is the owner of
        the questionnaire.
        Avoids users to update questionnaires that are not theirs.
        @author: Samuel de Lucas
        '''
        return self.get_object().user == self.request.user


class QuestionnaireCreateView (LoginRequiredMixin, CreateView):
    '''View to create a questionnaire. Only includes the title field.'''
    model = Questionnaire
    fields = ['title']
    success_url = reverse_lazy('questionnaire-list')

    def form_valid(self, form):
        '''
        Checks that the form is valid. Sets the user of the
        questionnaire to the logged in user.
        @author: Bhavuk Sikka
        '''
        form.instance.user = self.request.user
        return super(QuestionnaireCreateView, self).form_valid(form)


class QuestionDetailView (LoginRequiredMixin,
                          UserPassesTestMixin,
                          generic.DetailView):
    '''
    View to show the details of a question.
    Shows the question and the answers to the question.
    '''
    model = Question

    def get_context_data(self, **kwargs):
        '''
        Get context. Includes the answers of the question and
        the question itself.
        @author: Samuel de Lucas
        '''
        context = super().get_context_data(**kwargs)
        context['answer_list'] = self.object.answer_set.all()
        return context

    def test_func(self):
        '''
        Test function. Checks if the logged in user is
        the owner of the questionnaire corresponding to the question.
        Avoids users to see questions that are not theirs.
        @author: Samuel de Lucas
        '''
        return self.get_object().questionnaire.user == self.request.user


class QuestionRemoveView (LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''
    View to remove a question.
    Redirects to the questionnaire detail view of the questionnaire
    '''
    model = Question

    def get_success_url(self) -> str:
        '''
        Returns the url of questionnaire detail to redirect to
        after the delete is successful.
        @author: Bhavuk Sikka
        '''
        return reverse('questionnaire-detail',
                       kwargs={'pk': self.object.questionnaire.pk})

    def test_func(self):
        '''
        Test function. Checks if the logged in user is
        the owner of the questionnaire.
        Avoids users to delete questions that are not theirs.
        @author: Samuel de Lucas
        '''
        return self.get_object().questionnaire.user == self.request.user


class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''View to update a question.'''
    model = Question
    fields = ['question', 'answerTime']

    def get_context_data(self, **kwargs):
        '''
        Get context. Includes the question of the answer.
        Sets the isUpdate variable to True to show the correct template.
        @author: Bhavuk Sikka
        '''
        context = super().get_context_data(**kwargs)
        context['isUpdate'] = True
        return context

    def get_success_url(self) -> str:
        '''
        Returns the url of questionnaire detail to redirect to
        after the update is successful.
        @author: Bhavuk Sikka
        '''
        return reverse('question-detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        '''
        Test function. Checks if the logged in user is
        the owner of the questionnaire corre.
        Avoids users to updating questions that are not theirs.
        @author: Samuel de Lucas
        '''
        return self.get_object().questionnaire.user == self.request.user


class QuestionCreateView (LoginRequiredMixin, UserPassesTestMixin, CreateView):
    '''View to create a question.'''
    model = Question
    fields = ['question', 'answerTime']

    def form_valid(self, form):
        '''
        Checks that the form is valid.
        Sets the user of the question to the logged in user.
        Sets the questionnaire of the question to the questionnaire
        corresponding.
        @author: Bhavuk Sikka
        '''
        form.instance.user = self.request.user
        form.instance.questionnaire = Questionnaire.objects.get(
            pk=self.kwargs['questionnaireid'])
        return super(QuestionCreateView, self).form_valid(form)

    def get_success_url(self) -> str:
        '''
        Returns the url of questionnaire detail to redirect to
        after the create is successful.
        @author: Bhavuk Sikka
        '''
        return reverse('questionnaire-detail',
                       kwargs={'pk': self.object.questionnaire.pk})

    def test_func(self):
        '''
        Test function. Checks if the logged in user is
        the owner of the questionnaire corre.
        Avoids users to creating questions in questionnaires
        that are not theirs.
        @author: Samuel de Lucas
        '''
        return Questionnaire.objects.get(
            pk=self.kwargs['questionnaireid']).user == self.request.user


class AnswerCreateView (LoginRequiredMixin, UserPassesTestMixin, CreateView):
    '''View to create an answer.'''
    model = Answer
    fields = ['answer', 'correct']

    def get_context_data(self, **kwargs):
        '''
        Get context. Includes the question of the answer.
        @author: Bhavuk Sikka
        '''
        context = super().get_context_data(**kwargs)
        context['question'] = Question.objects.get(
            pk=self.kwargs['questionid'])
        success_url = reverse('question-detail',
                              kwargs={'pk': self.kwargs['questionid']})
        context['back_url'] = success_url
        return context

    def form_valid(self, form):
        '''
        Checks that the form is valid.
        Sets the user of the answer to the logged in user.
        Sets the question of the answer to the question corresponding.
        Checks that there are no more than 4 answers and that
        there is only one correct answer.
        @author: Samuel de Lucas
        '''
        form.instance.user = self.request.user
        form.instance.question = Question.objects.get(
            pk=self.kwargs['questionid'])
        if Answer.objects.filter(question=form.instance.question).count() >= 4:
            form.add_error(None, 'There can only be a maximum of 4 answers')
            return super(AnswerCreateView, self).form_invalid(form)
        if form.instance.correct:
            answers = Answer.objects.filter(question=form.instance.question,
                                            correct=True)
            if answers.count() > 0 and self.object not in answers:
                form.add_error(
                    'correct', 'There is already a correct answer defined')
                return super(AnswerCreateView, self).form_invalid(form)

        return super(AnswerCreateView, self).form_valid(form)

    def get_success_url(self) -> str:
        '''
        Returns the url of question detail to redirect to
        after the create is successful.
        @author: Bhavuk Sikka
        '''
        return reverse('question-detail',
                       kwargs={'pk': self.object.question.pk})

    def test_func(self):
        '''
        Test function. Checks if the logged in user is
        the owner of the questionnaire corresponding to the question.
        @author: Samuel de Lucas
        '''
        return Question.objects.get(
            pk=self.kwargs['questionid']
        ).questionnaire.user == self.request.user


class AnswerRemoveView (LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''View to remove an answer.'''
    model = Answer

    def get_success_url(self) -> str:
        '''
        Returns the url of question detail to redirect to
        after the delete is successful.
        @author: Bhavuk Sikka
        '''
        return reverse('question-detail',
                       kwargs={'pk': self.object.question.pk})

    def test_func(self):
        '''
        Test function. Checks if the logged in user is
        the owner of the questionnaire corresponding to the answer.
        @author: Samuel de Lucas
        '''
        return self.get_object().question.\
            questionnaire.user == self.request.user


class AnswerUpdateView (LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''View to update an answer.'''
    model = Answer
    fields = ['answer', 'correct']

    def get_context_data(self, **kwargs):
        '''
        Get context. Includes the question of the answer.
        Sets the isUpdate variable to True to show the correct template.
        @author: Bhavuk Sikka
        '''
        context = super().get_context_data(**kwargs)
        context['isUpdate'] = True
        context['question'] = self.object.question
        context['back_url'] = self.get_success_url()
        return context

    def get_success_url(self) -> str:
        '''
        Returns the url of question detail to redirect to
        after the update is successful.
        @author: Bhavuk Sikka
        '''
        return reverse('question-detail',
                       kwargs={'pk': self.object.question.pk})

    def test_func(self):
        '''
        Test function. Checks if the logged in user is
        the owner of the questionnaire corresponding to the answer.
        Avoids users to updating questions that are not theirs.
        @author: Samuel de Lucas
        '''
        return self.get_object().question.\
            questionnaire.user == self.request.user

    def form_valid(self, form):
        '''
        Checks that the form is valid.
        Sets the user of the answer to the logged in user.
        Sets the question of the answer to the question corresponding.
        Checks that there are no more than 4 answers and that
        there is only one correct answer.
        @author: Samuel de Lucas
        '''
        form.instance.user = self.request.user
        form.instance.question = self.object.question
        if form.instance.correct:
            answers = Answer.objects.filter(question=form.instance.question,
                                            correct=True)
            if answers.count() > 0 and self.object not in answers:
                form.add_error(
                    'correct', 'There is already a correct answer defined')
                return super(AnswerUpdateView, self).form_invalid(form)

        return super(AnswerUpdateView, self).form_valid(form)


class GameCreateView (LoginRequiredMixin, generic.View):
    '''View to create a game.'''
    model = Game
    template_name = 'models/game_create.html'

    def get(self, request, *args, **kwargs):
        '''
        Get method. Creates the game and shows the
        template with the corresponding pin.
        @author: Samuel de Lucas
        '''

        # get the questionnaire and add it to context
        q_id = self.kwargs['questionnaireid']
        questionnaire = get_object_or_404(Questionnaire, pk=q_id)
        context = {'questionnaire': questionnaire}

        if questionnaire.user == request.user:
            # create game
            game = Game(questionnaire=questionnaire)
            game.save()
            request.session['publicId'] = game.publicId

            context['game'] = game
            context['pin'] = game.publicId
            context['update_participant_url'] = request.build_absolute_uri(
                reverse('game-updateparticipant',
                        kwargs={'publicid': game.publicId}))
            context['game_join_url'] = GAME_JOIN_URL

        return render(request, self.template_name, context=context)


class GameUpdateParticipantView (LoginRequiredMixin, generic.View):
    '''
    View to get the participants of a game.
    Used in the game_create template to update the
    participants list in real time.
    '''
    model = Participant

    def get(self, request, *args, **kwargs):
        '''
        Get method. Returns the participants of the game in json format.
        @author: Samuel de Lucas
        '''
        try:
            if 'publicid' in self.kwargs:
                publicId = self.kwargs['publicid']
            else:
                publicId = request.session['publicId']
        except KeyError:
            return JsonResponse(
                {'error': 'No publicId for the game found. That might ' +
                 'be because the game does not belong to logged ' +
                 'user, or because the game has not been created yet.'})

        game = Game.objects.get(publicId=publicId)
        if game.questionnaire.user != request.user:
            return JsonResponse({'error': 'This game does not belong to ' +
                                 'logged user'})
        participants = list(
            Participant.objects.filter(game__publicId=publicId))
        serialized_data = serializers.serialize('json', participants)
        return JsonResponse({'participants': serialized_data})


class GameCountdownView (LoginRequiredMixin, UserPassesTestMixin,
                         generic.View):
    '''View to show the countdown before the game starts.'''
    model = Game

    def test_func(self):
        '''
        Test function. Checks if the logged in user is
        the owner of the questionnaire corresponding to the game.
        Avoids users to updating questions that are not theirs.
        @author: Samuel de Lucas
        '''
        try:
            game = Game.objects.get(publicId=self.request.session['publicId'])
        except KeyError:
            return False
        return game.questionnaire.user == self.request.user

    def get_context_data(self, **kwargs):
        '''
        Get context. Includes the game and the remaining time
        to refresh the page (used in JS).
        Includes different data depending on the game state.
        @author: Samuel de Lucas
        '''
        context = {}
        game = get_object_or_404(
            Game, publicId=self.request.session['publicId'])
        context['game'] = game

        # WAITING
        if game.state == WAITING:
            # remainingTime will contain the time left to start the game
            #   It is calulated as the countdown time minus the time elapsed
            remainingTime = timedelta(seconds=game.countdownTime) - \
                (datetime.now(timezone.utc) - game.lastTimeButtonPressed)

            # if the remaining time is negative, the game has already started,
            #  so we indicate to the caller that the state should change
            if remainingTime.total_seconds() < 0:
                raise Game.ChangeState()

            # if there is time left, we add it to the context
            context['remainingTime'] = remainingTime.total_seconds()

        # QUESTION
        elif game.state == QUESTION:
            # get the current question/answers
            q_list = list(Question.objects.filter(
                questionnaire=game.questionnaire))
            question = q_list[game.questionNo]
            answers = list(Answer.objects.filter(question=question))

            # remainingTime will contain the remaining time to keep showing
            #  the question. It is calculated as
            remainingTime = timedelta(seconds=question.answerTime) - \
                (datetime.now(timezone.utc) - game.lastTimeButtonPressed)

            # if the remaining time is negative, the game has already started,
            #  so we indicate to the caller that the state should change
            if remainingTime.total_seconds() < 0:
                raise Game.ChangeState()

            # if there is time left, we add it to the context
            context['remainingTime'] = remainingTime.total_seconds()
            context['question'] = question
            context['answers'] = answers

        elif game.state == ANSWER:
            # get the current question
            q_list = list(Question.objects.filter(
                questionnaire=game.questionnaire))
            question = q_list[game.questionNo]
            context['question'] = question

            # we add the answers to the context
            # Note that there should be only one correct answer
            # but we take into account the possibility of having more
            # in case of error
            answers = question.answer_set.all()
            context['answers'] = answers
            context['noneCorrect'] = not any((a.correct for a in answers))

            # add the leaderboard to the context
            context['participants'] = list(
                Participant.objects.filter(game=game).order_by('-points'))

            # if the current question is the last one, we add the
            #   leaderboard_next variable to the context
            total_questions = game.questionnaire.question_set.count()
            if game.questionNo == total_questions - 1:
                context['leaderboard_next'] = True

        # LEADERBOARD
        elif game.state == LEADERBOARD:
            # add the leaderboard to the context
            context['participants'] = list(
                Participant.objects.filter(game=game).order_by('-points'))

        return context

    def get_next_state(self, game):
        '''
        Get the next state of the game.
        @author: Samuel de Lucas
        '''
        if game.state == WAITING:
            if game.questionnaire.question_set.count() > 0:
                # WAITING -> QUESTION (if there are questions)
                return QUESTION
        elif game.state == QUESTION:
            # QUESTION -> ANSWER
            return ANSWER
        elif game.state == ANSWER:
            # ANSWER -> QUESTION (if there are more questions)
            if game.questionNo < game.questionnaire.question_set.count() - 1:
                game.questionNo += 1
                return QUESTION
        # ANSWER -> LEADERBOARD (if there are no more questions)
        return LEADERBOARD

    def get_template_names(self):
        '''
        Get the template name depending on the game state.
        @author: Samuel de Lucas
        '''
        game = Game.objects.get(publicId=self.request.session['publicId'])
        if game.state == WAITING:
            return 'models/game_waiting.html'
        elif game.state == QUESTION:
            return 'models/game_question.html'
        elif game.state == ANSWER:
            return 'models/game_answer.html'
        elif game.state == LEADERBOARD:
            return 'models/game_leaderboard.html'

    def get(self, request, *args, **kwargs):
        '''
        Get the game state and render the corresponding template.
        If the game state must change, reload the page.
        @author: Bhavuk Sikka
        '''
        try:
            context = self.get_context_data(**kwargs)
        except Game.ChangeState:
            game = get_object_or_404(
                Game, publicId=request.session['publicId'])
            game.state = self.get_next_state(game)
            game.save()
            return redirect('game-count-down')

        return render(request, self.get_template_names(), context=context)

    def post(self, request, *args, **kwargs):
        '''
        Modify game when "Launch game" or "Next question" buttons are
        pressed. Redirect to the game page.
        @autor: Bhavuk Sikka
        '''
        game = get_object_or_404(
            Game, publicId=request.session['publicId'])

        # differenciate between the two waiting states
        # by checking if the "launch", which are before waiting and after
        # waiting time (game.coundownTime)
        if game.state == WAITING and 'launch' not in request.POST:
            remainingTime = timedelta(seconds=game.countdownTime) - \
                (datetime.now(timezone.utc) - game.lastTimeButtonPressed)
            if remainingTime.total_seconds() < 0:
                game.state = self.get_next_state(game)

        elif game.state == ANSWER:
            game.state = self.get_next_state(game)

        game.lastTimeButtonPressed = datetime.now(timezone.utc)
        game.save()

        return redirect('game-count-down')
