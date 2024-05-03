from os import walk
from chat.models import Chat, Message
from django.db import IntegrityError
from django.shortcuts import render
from django.http import  HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST':
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages':chatMessages})

def login_view(request):
    redirect = request.GET.get('next')
    if request.method == 'POST':
            user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.POST.get('redirect'))
            else:
                return render(request, 'auth/login.html', {'wrongPassword': True, 'redirect': redirect})
    return render(request, 'auth/login.html', {'redirect': redirect})

def registration_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if password :
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                print(user)
                return render(request, 'auth/login.html', {'registrationSuccess':True})
            except IntegrityError:
                return render(request, 'auth/registration.html', {'existingEmailOrUser':True})
        else:
            return render(request, 'auth/registration.html', {'existingEmailOrUser':False})
    return render(request, 'auth/registration.html', {redirect: redirect})
