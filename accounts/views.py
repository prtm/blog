# core django
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django import forms
from django.http import HttpResponse


# project
from .forms import UserRegistrationForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                u = User.objects.create_user(username, email, password)
                # add logic or permissions for newly created user
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponse('Dashboard')
                # return redirect(':dashboard')
            else:
                raise forms.ValidationError(
                    'username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
