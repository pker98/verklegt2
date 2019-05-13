from django import forms
from django.forms import ModelForm, widgets
from greidsla.models import Payment

class GreidsluferliForm(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'cardnumber': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'ccv': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'date_of_expiration': widgets.SelectDateWidget(empty_label=("Ár", "Mán"))
        }
        labels={
            'name': 'Korthafi',
            'cardnumber': 'Kortanúmer',
            'ccv': 'Öryggisnúmer (CCV)',
            'date_of_expiration': 'Gildistími'
        }
