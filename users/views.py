from django.shortcuts import render, redirect
from .models import Profile


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
