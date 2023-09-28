from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def userIndex (request):
    # return HttpResponse("esta es la pagina principal de usuarios")
    return render(request, 'proyecto/index.html')

def profile (request, user='ejemplo'):
    return render(request, 'users/profile.html', {"user":user,})

def mail (request, user='ejemplo'):
    return render(request, 'users/mail.html', {'user':user,})