from django.forms import ModelForm, widgets
from notandi.models import ProfileImage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class ProfileImageForm(ModelForm):
    class Meta:
        model = ProfileImage
        exclude = ['id', 'user_id', 'user']
        widgets = {
            'profile_img': widgets.URLInput(attrs={'class': 'form-control'})
        }
        labels = {
            'profile_img': 'Profile Mynd'
        }

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'groups',
                   'user_permissions', 'password']
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'form-control'}),
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'}),
            'image': forms.CharField(required=True, widget=forms.TextInput(attrs={ 'class': 'form-control' }))
        }


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']