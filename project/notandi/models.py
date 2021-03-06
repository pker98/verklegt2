from django.db import models
from django.contrib.auth.models import User

class ProfileImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_img = models.CharField(max_length=9999)

    def __str__(self):
        return self.profile_img

    #Need to be able to get the email and name into the form here
    #to be able to change them. Can't figure out how to connect
    #to the user table and change those at the same time
    #Also need to figure out how to change the look of the text in the
    #html view so it doesnt just display profile img
