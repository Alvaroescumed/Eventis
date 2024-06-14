from django.db import models
from events.models import Concert, Festival
import uuid


class User(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birth_date= models.DateField()
    mail = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name
