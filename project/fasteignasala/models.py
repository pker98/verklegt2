from django.db import models
from django.contrib.auth.models import User

# class Base_user(models.Model):
#    name = models.CharField(max_length=55)

# class SalesUser(models.Model):
#    description = models.CharField(max_length=255)

# class PaymentInfo(models.Model):
#    bank_account_num = models.CharField(max_length=999)


class Apartment(models.Model):
    address = models.CharField(max_length=255)
    price = models.IntegerField()
    fire_insurance = models.IntegerField()
    estimated_value = models.IntegerField()
    type = models.CharField(max_length=255)
    size = models.IntegerField()
    num_rooms = models.IntegerField()
    num_bed_room = models.IntegerField()
    num_bath_room = models.IntegerField()
    description = models.CharField(max_length=600)
    zip = models.IntegerField(blank=False)
    town = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.address


class ApartmentImage(models.Model):
    image = models.CharField(max_length=999)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)

    def __str__(self):
        return self.image

# class Base_userImage(models.Model):
#    image = models.CharField(max_length=999)
#   salesman = models.ForeignKey(Sales_user, on_delete=models.CASCADE)

# class Sales_userImage(models.Model):
#    image = models.CharField(max_length=999)
#   salesman = models.ForeignKey(Sales_user, on_delete=models.CASCADE)






