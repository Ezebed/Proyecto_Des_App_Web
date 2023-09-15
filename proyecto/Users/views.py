from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def userIndex (request):
    return HttpResponse("esta es la pagina principal de usuarios")