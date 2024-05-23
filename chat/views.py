from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.utils import timezone

from chat.models import Chat, Message


# Create your views here.
@login_required(login_url='/login/')
def index(request):
    """create a new message and renders the side"""
    if request.method == 'POST':
        my_chat = Chat.objects.get(id=1)
        new_message = Message.objects.create(
                text=request.POST['textmessage'],
                chat=my_chat,
                author=request.user,
                receiver=request.user,
                created_at=timezone.now()
                )
        serialized_object = serializers.serialize('json', [ new_message, ])
        return JsonResponse(serialized_object[1:-1], safe=False)
    chat_messages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages':chat_messages})

def login_view(request):
    """handle login"""
    redirect = request.GET.get('next')
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect(request.POST.get('redirect'))
        return render(request, 'auth/login.html', {'wrongPassword': True, 'redirect': redirect})
    return render(request, 'auth/login.html', {'redirect': redirect})

def registration_view(request):
    """handle registration"""
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
    return render(request, 'auth/registration.html')
