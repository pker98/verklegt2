from django.forms import ModelForm, widgets
from django import forms
from fasteignasala.models import Apartment

class HusnaediUpdateForm(forms.ModelForm):
    class Meta:
        model = Apartment
        exclude = ['id']
        widgets = {
            'address': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'price': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'fire_insurance': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'estimated_value': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'zip': widgets.NumberInput(attrs={'class': 'form-control' }),
            'town': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'type': widgets.Select(choices={('Einbýlishús', 'Einbýlishús'),('Tvíbýlishús','Tvíbýlishús'),('Fjölbýlishús', 'Fjölbýlishús')}),
            'size': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'num_rooms': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'num_bed_room': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'num_bath_room': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'description': widgets.TextInput(attrs={ 'class': 'form-control' })
        }
        labels = {
            'address': 'Húsnæði',
            'price': 'Verð',
            'fire_insurance': 'Brunabótamat',
            'estimated_value': 'Fasteignamat',
            'zip': 'Póstnúmer',
            'town': 'Bær',
            'type': 'Tegund',
            'size': 'Stærð',
            'num_rooms': 'Fjöldi herbergja',
            'num_bed_room': 'Fjöldi svefnherbergja',
            'num_bath_room': 'Fjöldi baðherbergja',
            'description': 'Lýsing',
            'image': 'Myndir'
        }

class HusnaediCreateForm(forms.ModelForm):
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
            'town': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'type': widgets.Select(choices={('1', 'Einbýlishús'),('2','Tvíbýlishús'),('3', 'Fjölbýlishús')}),
            'size': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'num_rooms': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'num_bed_room': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'num_bath_room': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'description': widgets.TextInput(attrs={ 'class': 'form-control' })
        }
        labels = {
            'address': 'Húsnæði',
            'price': 'Verð',
            'fire_insurance': 'Brunabótamat',
            'estimated_value': 'Fasteignamat',
            'zip': 'Póstnúmer',
            'town': 'Bær',
            'type': 'Tegund',
            'size': 'Stærð',
            'num_rooms': 'Fjöldi herbergja',
            'num_bed_room': 'Fjöldi svefnherbergja',
            'num_bath_room': 'Fjöldi baðherbergja',
            'description': 'Lýsing',
            'image': 'Myndir'

        }