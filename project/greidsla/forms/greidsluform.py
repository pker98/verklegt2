from django import forms
from django.forms import ModelForm, widgets
from greidsla.models import Buyer

class GreidsluferliForm(ModelForm):
    class Meta:
        model = Buyer
        exclude = ['id', 'user_id']
        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'ssn': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.NumberInput(attrs={'class': 'form-control'}),
            'phone': widgets.NumberInput(attrs={'class': 'form-control'}),
            'pay_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'date_of_expiration': widgets.SelectDateWidget(empty_label=("Ár", "Mán", "Dagur")),
            'ccv': widgets.NumberInput(attrs={ 'class': 'form-control'})
        }
        labels = {
            'name': 'Fullt nafn',
            'ssn': 'Kennitala',
            'address': 'Heimilisfang',
            'zip': 'Póstnúmer',
            'phone': 'Sími',
            'pay_name': 'Korthafi',
            'cardnumber': 'Kortanúmer',
            'ccv': 'Öryggisnúmer (CCV)',
            'date_of_expiration': 'Gildistími'
        }

