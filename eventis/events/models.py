from django.db import models
from users.models import *


class Artist(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

#creamos un modelo plantilla para los eventos
class Event(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=240)
    date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # Solo para festivales
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    artists = models.ManyToManyField(Artist)
    

    def __str__(self):
        return self.name
    

# Creamos el modelo de entrada

    
class Assistants(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event  = models.ForeignKey('Event', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} entrada para {self.event.name}"