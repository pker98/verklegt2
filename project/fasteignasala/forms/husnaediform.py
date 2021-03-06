from django.forms import ModelForm, widgets
from django import forms
from fasteignasala.models import Apartment

class HusnaediUpdateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    class Meta:
        model = Apartment
        exclude = ['id']
        widgets = {
            'address': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'price': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'fire_insurance': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'estimated_value': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'zip': widgets.Select(choices={('101', '101'),('170','170'),('190', '190'), ('200', '200'), ('210', '210'),
            ('220', '220'), ('225', '225'), ('230', '230'), ('245', '245'), ('270', '270'), ('300', '300'), ('400', '400'),
                                           ('580', '580'), ('600', '600')}),
            'town': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'type': widgets.Select(choices={('Einbýlishús', 'Einbýlishús'),('Tvíbýlishús','Tvíbýlishús'),('Fjölbýlishús', 'Fjölbýlishús')}),
            'size': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'num_rooms': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'num_bed_room': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'num_bath_room': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'description': widgets.TextInput(attrs={ 'class': 'form-control' })
        }
        labels = {
            'address': 'Heimilisfang',
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

class HusnaediCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    class Meta:
        model = Apartment
        exclude = [ 'id', 'seller' ]
        widgets = {
            'address': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'price': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'fire_insurance': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'estimated_value': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'zip': widgets.Select(choices={('101', '101'),('170','170'),('190', '190'), ('200', '200'), ('210', '210'),
            ('220', '220'), ('225', '225'), ('230', '230'), ('245', '245'), ('270', '270'), ('300', '300'), ('400', '400'),
                                           ('580', '580'), ('600', '600')}),
            'town': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'type': widgets.Select(choices={('Einbýlishús', 'Einbýlishús'),('Tvíbýlishús','Tvíbýlishús'),('Fjölbýlishús', 'Fjölbýlishús')}),
            'size': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'num_rooms': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'num_bed_room': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'num_bath_room': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'description': widgets.TextInput(attrs={ 'class': 'form-control' })
        }
        labels = {
            'address': 'Heimilisfang',
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