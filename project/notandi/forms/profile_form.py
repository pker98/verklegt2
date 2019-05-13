from django.forms import ModelForm, widgets
from notandi.models import Profile

class Profile_form(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'profile_img': widgets.TextInput(attrs={'class' : 'form-control'})
        }

