from django.db import models
from django.contrib.auth.models import User

class Base_user(models.Model):
    name = models.CharField(max_length=255)
    SSN = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Sales_user(models.Model):
    description = models.CharField(max_length=255)
    user = models.ForeignKey(Base_user, on_delete=models.CASCADE)

class Apartment(models.Model):
    description = models.CharField(max_length=255)
    salesman = models.ForeignKey(Sales_user, on_delete=models.CASCADE)

class ApartmentImage(models.Model):
    image = models.CharField(max_length=999)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)

class SalesmanImage(models.Model):
    image = models.CharField(max_length=999)
    salesman = models.ForeignKey(Sales_user, on_delete=models.CASCADE)
