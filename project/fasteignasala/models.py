from django.db import models
from django.contrib.auth.models import User

class Base_user(models.Model):
    SSN = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=999)
    def __str__(self):
        return self.name

class Sales_user(models.Model):
    description = models.CharField(max_length=255)

class Payment_info(models.Model):
    bank_account_num = models.CharField(max_length=999)

class Apartment(models.Model):
    address = models.CharField(max_length=255)
    price = models.CharField(max_length=20)
    fire_insurance = models.CharField(max_length=20)
    type = models.CharField(max_length=255)
    num_rooms = models.CharField(max_length=2)
    size = models.CharField(max_length=255)
    num_living_room = models.CharField(max_length=2)_
    num_bed_room = models.CharField(max_length=2)
    num_bath_room = models.CharField(max_length=2)
    description = models.CharField(max_length=600)

class ApartmentImage(models.Model):
    image = models.CharField(max_length=999)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)

class Base_userImage(models.Model):
    image = models.CharField(max_length=999)
    salesman = models.ForeignKey(Sales_user, on_delete=models.CASCADE)

class Sales_userImage(models.Model):
    image = models.CharField(max_length=999)
    salesman = models.ForeignKey(Sales_user, on_delete=models.CASCADE)
