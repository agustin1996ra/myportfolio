from django.db import models
from PIL import Image

class Album(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=200)

    def __str__(self):
        return self.caption

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Abre la imagen usando Pillow
        img = Image.open(self.image.path)

        # Redimensiona la imagen si es necesario
        if img.height > 800 or img.width > 800:
            output_size = (800, 800)
            img.thumbnail(output_size)
            img.save(self.image.path)
