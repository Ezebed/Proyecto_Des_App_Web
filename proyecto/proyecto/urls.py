"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from proyecto.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # path( "como se va a ver la URL" , <nombre de la vista>, name=<nombre interno de esta direccion> )
    # ejemplo: esta direccion se veria de esta manera en el navegador
    # 127.0.0.1
    path("", index, name="index"),

    # con include coloco todas las urls del modulo User/urls.py y se agregan al final de la ruta
    # ex: 127.0.0.1/Usuarios/<URLS de Users>
    path("usuarios/", include('Users.urls')),

    # prueba de una redireccion a partir del nombre de la misma
    path('redireccionPrueba/', redireccionPrueba )
]
