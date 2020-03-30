from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm, MessageForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('messages')
    return render(request, 'index.html', {})

@login_required
def user_messages(request):
    # filter messages according to currently logged in user.
    messages_qs = Message.objects.filter(owner=request.user).order_by('-time_stamp')

    return render(request, 'messages.html', {'messages' : messages_qs})


def send_message(request, user):
    try_user = get_object_or_404(User, username=user)
    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.instance.owner = User.objects.get(username=user)
        form.save()
        messages.success(request, 'Your message has been sent.')
        return redirect('register')
    return render(request, 'send_message.html', {'form' : form, 'user' : user })


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(request, user)
        return redirect('index')
    return render(request, 'register.html', {'form' : form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('index')
    return render(request, 'login.html', {'form' : form})

def logout_view(request):
    logout(request)
    return redirect('index')