from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birth_date= models.DateField()
    mail = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)