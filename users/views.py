from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import RegisterForm, ProfileForm


def sign_in(request):
    page = 'sign_in'
    if request.user.is_authenticated:
        return redirect('user_profile', pk=request.user.profile.id)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except Exception:
            messages.error(request, 'Username does not exist!')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_profile', pk=request.user.profile.id)
        else:
            messages.error(request, 'Username OR Password is incorrect!')

    context = {
        'page': page
        }
    return render(request, 'users/sign_in.html', context)


def sign_out(request):
    logout(request)
    messages.success(request, 'User was successfuly signed out!')
    return redirect('sign_in')


def register(request):
    page = 'register'
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account created!')
            login(request, user)
            return redirect('edit_account')
        else:
            messages.error(request, 'Ooops something went wrong!')
    context = {
        'page': page,
        'form': form
    }
    return render(request, 'users/sign_in.html', context)


def profiles(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'users/profiles.html', context)


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {
        'profile': profile
    }
    return render(request, 'users/user_profile.html', context)


@login_required(login_url='sign_in')
def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile', pk=profile.id)
    context = {
        'form': form
    }
    return render(request, 'users/profile_form.html', context)
