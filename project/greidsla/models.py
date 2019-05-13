from django.db import models

# Create your models here.
class Payment(models.Model):
    name = models.CharField(max_length=60)
    card_number = models.CharField(max_length=16)
    ccv = models.CharField(max_length=3)
    date_of_expiration = models.DateField(max_length=8)

    def __str__(self):
        return self.address

class Buyer(models.Model):
    name = models.CharField(max_length=60)
    ssn = models.CharField(max_length=10)
    street_name = models.CharField(max_length=50)
    house_num = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip = models.CharField(max_length=50)

    def __str__(self):
        return self.name