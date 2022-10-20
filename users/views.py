from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Profile, Message
from .forms import RegisterForm, ProfileForm, MessageForm
from .utils import search_profiles, profile_pagination


def landingpage(request):
    return render(request, 'landingpage.html')


def sign_in(request):
    page = 'sign_in'
    if request.user.is_authenticated:
        return redirect('user_profile', pk=request.user.profile.id)

    if request.method == 'POST':
        username = request.POST['username'].lower()
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
    messages.success(request, 'User was successfully signed out!')
    return redirect('sign_in')


def register(request):
    if request.user.is_authenticated:
        return redirect('user_profile', pk=request.user.profile.id)
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


@login_required(login_url='sign_in')
def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated!')
            return redirect('user_profile', pk=profile.id)
    context = {
        'form': form
    }
    return render(request, 'users/profile_form.html', context)


@login_required(login_url='sign_in')
def delete_account(request):
    profile = request.user.profile
    if request.method == 'POST':
        profile.delete()
        messages.success(request, 'Account Deleted!')
        return redirect('landingpage')
    return render(request, 'users/delete_user.html')


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {
        'profile': profile
    }
    return render(request, 'users/user_profile.html', context)


def profiles(request):
    profiles, search_query = search_profiles(request)
    custom_range, profiles = profile_pagination(request, profiles, 6)

    context = {
        'profiles': profiles,
        'search_query': search_query,
        'custom_range': custom_range
    }
    return render(request, 'users/profiles.html', context)


@login_required(login_url='sign_up')
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    context = {
        'messageRequests': messageRequests,
        'unreadCount': unreadCount
    }
    return render(request, 'users/inbox.html', context)


@login_required(login_url='sign_up')
def view_message(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read is False:
        message.is_read = True
        message.save()
    context = {
        'message': message
    }
    return render(request, 'users/message.html', context)


def create_message(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()

    try:
        sender = request.user.profile
    except Exception:
        sender = None

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()

            messages.success(request, 'Message sent!')
            return redirect('user_profile', pk=recipient.id)
    context = {
        'recipient': recipient,
        'form': form
    }
    return render(request, 'users/message_form.html', context)


@login_required(login_url='login')
def delete_message(request, pk):
    page = 'delete'
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if request.method == 'POST':
        message.delete()
        return redirect('inbox')
    context = {
        'object': message.name,
        'page': page
        }
    return render(request, 'recipeapp/delete_object.html', context)


@login_required(login_url='login')
def reply_message(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()

    try:
        sender = request.user.profile
    except Exception:
        sender = None

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()

            messages.success(request, 'Message sent!')
            return redirect('inbox')

    context = {
        'recipient': recipient,
        'form': form
        }
    return render(request, 'users/message_form.html', context)
