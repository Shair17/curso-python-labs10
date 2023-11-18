from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Post(models.Model):
  titulo = models.CharField(max_length=255)
  descripcion = models.CharField(max_length=255)
  contenido = HTMLField()
  fecha = models.DateField(auto_now_add=True)
  imagen = models.CharField(max_length=255)
  likes = models.ManyToManyField(User, related_name='likes', blank=True)