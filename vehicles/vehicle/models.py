from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.
class Vehicles(models.Model):
   engineStatus = models.CharField(max_length=150)
   fuelLevel = models.CharField(max_length=150)
   temperature = models.CharField(max_length=100)
   averageSpeed = models.IntegerField()
   speed = models.IntegerField()
   name = models.CharField(max_length=150)
class Switch(models.Model):
   id = models.AutoField(primary_key=True)