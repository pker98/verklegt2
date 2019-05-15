from django import forms
from django.forms import ModelForm, widgets
from greidsla.models import Payment

class GreidsluferliForm(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'ssn': widgets.NumberInput(attr={ 'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.NumberInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(choices={('Einbýlishús', 'Einbýlishús'),('Tvíbýlishús','Tvíbýlishús'),('Fjölbýlishús', 'Fjölbýlishús')}),
            'phone': widgets.NumberInput(attrs={'class': 'form-control'}),
            'pay_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.NumberInput(attrs={ 'class': 'form-control' }),
            'date_of_expiration': widgets.SelectDateWidget(empty_label=("Ár", "Mán")),
            'ccv': widgets.NumberInput(attrs={ 'class': 'form-control'})
        }
        labels={
            'name': 'Korthafi',
            'cardnumber': 'Kortanúmer',
            'ccv': 'Öryggisnúmer (CCV)',
            'date_of_expiration': 'Gildistími'
        }

