from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.messages import error
from django import forms

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            rawPassword = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=rawPassword)
            login(request, user)
            return redirect('choices')
    else:
        form = UserCreationForm()
    return render(request, 'changeActions/signup.html', {'form': form})

def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('choices')
    else:
        error(request, 'Please Enter a Valid Login')
        return redirect('choices')

def user_logout(request):
    logout(request)
    return redirect('choices')

def password_reset(request):
    return render(request, 'login/password_reset_form.html')


