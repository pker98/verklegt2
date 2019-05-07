from django.db import models
# from django.contrib.auth.models import User

class Apartment(models.Model):
    description = models.CharField(max_length=255)
    salesman = models.ForeignKey(User, on_delete=models.SET_NULL)

class ApartmentImage(models.Model):
    image = models.CharField(max_length=999)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)

# Create your models here.
