from django.forms import ModelForm, widgets
from notandi.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'user': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'profile_img': widgets.URLInput(attrs={'class': 'form-control'})
        }
        labels = {
            'user': 'Notandi',
            'email': 'Email',
            'profile_img': 'Profile Mynd'
        }


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']