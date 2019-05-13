from django.forms import ModelForm, widgets
from django import forms
from fasteignasala.models import Apartment

class HusnaediUpdateForm(ModelForm):
    class Meta:
        model = Apartment
        exclude = ['id']
        widgets = {
            'address': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'price': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'fire_insurance': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'estimated_value': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'zip': widgets.NumberInput(attrs={'class': 'form-control' }),
            'town': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'type': widgets.Select(attrs={ 'class': 'form-control' }),
            'size': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'num_rooms': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'num_bed_room': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'num_bath_room': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'description': widgets.TextInput(attrs={ 'class': 'form-control' })
        }

class HusnaediCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    class Meta:
        model = Apartment
        exclude = [ 'id' ]
        widgets = {
            'address': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'price': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'fire_insurance': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'estimated_value': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'zip': widgets.NumberInput(attrs={'class': 'form-control' }),
            'town': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'type': widgets.Select(attrs={ 'class': 'form-control' }),
            'size': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'num_rooms': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'num_bed_room': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'num_bath_room': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'description': widgets.TextInput(attrs={ 'class': 'form-control' })
        }
