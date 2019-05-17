from django.db import models
from django.contrib.auth.models import User

class Buyer(models.Model):
    name = models.CharField(max_length=60)
    ssn = models.IntegerField()
    address = models.CharField(max_length=50)
    zip = models.IntegerField()
    phone = models.IntegerField()
    pay_name = models.CharField(max_length=60)
    card_number = models.CharField(max_length=16)
    date_of_expiration = models.DateField(max_length=8)
    ccv = models.CharField(max_length=3)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name