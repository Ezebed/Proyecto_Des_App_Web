from django.contrib import admin
from django.urls import path
from Users.views import *

urlpatterns = [
    path('', userIndex, name='users'),
    path('<user>/profile/', profile, name="profile"),
    path('<user>/mail/', mail, name="mail"),
]