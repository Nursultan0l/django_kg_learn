from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import LoginForm, RegistrationForm, ProfileUpdateForm
from django.urls import reverse

def login(request):
    if request.method == 'POST':
        form = LoginForm(data= request.POST)
        if form.is_valid():
            user = getattr(form, 'user_cache', None)
            if user:
                auth.login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    auth.logout(request)
    return redirect('home')

@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})

def edit_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
    return redirect(request.META.get('HTTP_REFERER', 'home'))




