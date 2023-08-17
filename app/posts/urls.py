from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('albums/', views.v_albums, name="albums"),
    path('albums/photos/', views.v_photos, name="photos")
]

