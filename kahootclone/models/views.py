from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm


def signup(request):
    '''
    This view is used to register a new user.
    @author: Bhavuk Sikka
    '''
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():  # already checks password match
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
