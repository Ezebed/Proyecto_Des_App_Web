from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.template import loader

# vistas para la pagina principal
def index(request):
    # obtenemos la plantilla HTML de la pagina
    template = loader.get_template('proyecto/index.html')
    # cargamos las variables en formato json
    contex = { "nombreProyecto" : "Intranet de la UC" }
    # por ultimo retornamos la plantilla cargando el contexto que tiene el valor de las variables
    return HttpResponse(template.render(contex))



# prueba de como hacer una redireccion a otra vbista a partir del el nombre de la misma
def redireccionPrueba (request):
    return HttpResponseRedirect(reverse('index'))