from django.db import models
from fasteignasala.models import Apartment
from django.contrib.auth.models import User

# Create your models here.
class History(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    viewed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.apartment)