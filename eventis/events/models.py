from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

#creamos un modelo plantilla para los eventos
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=240)
    date = models.DateField()
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
    


class Concert(Event):
   artists = models.ManyToManyField(Artist, related_name='concert')

class Festival(Event):

    end_date = models.DateField()
    artists = models.ManyToManyField(Artist, related_name='festival')
