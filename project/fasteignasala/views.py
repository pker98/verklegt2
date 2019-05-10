from django.shortcuts import render, get_object_or_404

from fasteignasala.forms.husnaediform import HusnaediCreateForm
from fasteignasala.models import Apartment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView




def home(request):
    context = {"apartments" : Apartment.objects.all()}
    return render(request, 'forsida/home.html', context)

def get_apartm_by_id(request, id):
    return render(request, 'hus/husnaedi_details.html', {
    'apartment': get_object_or_404(Apartment, pk=id)
    })

def create_apartment(request):
    if request.method == 'POST':
        print(1)
    else:
        form = HusnaediCreateForm()
    return render(request, 'hus/nytt_husnaedi.html', {
        'form': form
    })


def um_okkur(request):
    return render(request, 'um_okkur/um_okkur.html', {"title": "Um okkur"})

def starfsmenn(request):
    return render(request, 'starfsmenn/starfsmenn.html', {"title": "Starfsmenn"})

def soluskra(request):
    return render(request, 'soluskra/soluskra.html', {"title": "Söluskrá"})
