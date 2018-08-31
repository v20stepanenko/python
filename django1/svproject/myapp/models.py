from django.db import models

# Create your models here.
class Person(models.Model):

    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    money = models.IntegerField()

class Auto(models.Model):

     license_number = models.CharField(max_length=10)
     vendor = models.CharField(max_length=10)
     person = models.ForeignKey(Person, on_delete=models.CASCADE)