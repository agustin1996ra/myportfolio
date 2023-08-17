from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Photo


def home(request):
    pagina_actual = 'home'
    albums = Album.objects.all()
    return render(request, 'home.html', {'pagina_actual': pagina_actual, 'albums': albums})


def v_albums(request):
    pagina_actual = 'proyectos'
    fotos = Photo.objects.all()
    return render(request, 'albums.html', {'pagina_actual': pagina_actual})


def v_photos(request):

    return render(request, 'photos.html', {})