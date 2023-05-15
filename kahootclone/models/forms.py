from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    '''Form for creating a user. Includes password confirmation.'''
    class Meta:
        '''
        Class that defines the model and the fields that will be
        shown in the form.
        '''
        model = get_user_model()
        fields = ('username', 'password1', 'password2')
