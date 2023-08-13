from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo


def home(request):
    pagina_actual = 'home'
    foto = Photo.objects.get(id=1)
    return render(request, 'home.html', {'pagina_actual': pagina_actual, 'foto': foto})


def proyectos(request):
    pagina_actual = 'proyectos'
    return render(request, 'proyectos.html', {'pagina_actual': pagina_actual})