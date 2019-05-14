from django.db import models

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from fasteignasala.models import Apartment
from notandi.models import User

class History(models.Model):
    user = models.ManyToManyField(User)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    viewed_on = models.DateTimeField(auto_now_add=True)

