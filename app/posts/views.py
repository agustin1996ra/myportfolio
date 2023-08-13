from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    pagina_actual = 'home'
    return render(request, 'home.html', {'pagina_actual': pagina_actual})


def proyectos(request):
    pagina_actual = 'proyectos'
    return render(request, 'proyectos.html', {'pagina_actual': pagina_actual})