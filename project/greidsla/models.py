from django.db import models

# Create your models here.
class Payment(models.Model):
    name = models.CharField(max_length=60)
    cardnumber = models.CharField(max_length=16)
    ccv = models.CharField(max_length=3)
    date_of_expiration = models.CharField(max_length=4)

    def __str__(self):
        return self.address