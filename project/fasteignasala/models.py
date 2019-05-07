from django.db import models
from django.contrib.auth.models import User

class base_user(models.Model):
    name = models.CharField(max_length=255)
    SSN = models.CharField(max_length=10)

class Sales_user(models.Model):
    pass

class Salesman(models.Model):
    description = models.CharField(max_length=255)
    user = models.ForeignKey(base_user, on_delete=models.CASCADE)

class Apartment(models.Model):
    description = models.CharField(max_length=255)
    salesman = models.ForeignKey(Sales_user, on_delete=models.CASCADE)

class ApartmentImage(models.Model):
    image = models.CharField(max_length=999)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)

# Create your models here.
