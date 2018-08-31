from django.db import models


# Create your models here.

class Address(models.Model):

    def __str__(self):
        return '{0} - {1}'.format(self.country, self.city)

    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    house_number = models.CharField(max_length=30)
    flat = models.CharField(max_length=30)
