from django.db import models
from PIL import Image

class Album(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to = "static/album_photo/", default="")
    destacado = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.title

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/photos/')
    caption = models.CharField(max_length=200)

    def __str__(self):
        return self.caption

    