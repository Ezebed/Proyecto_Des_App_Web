from django.contrib import admin
from django.urls import path
from Users.views import *

urlpatterns = [
    path('', userIndex, name='users'),
    path('profile/<user>/', profile, name="profile"),
]