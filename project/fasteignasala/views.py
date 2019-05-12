from django.shortcuts import render, get_object_or_404, redirect
from fasteignasala.forms.husnaediform import HusnaediCreateForm
from fasteignasala.models import Apartment, ApartmentImage
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
        form = HusnaediCreateForm(data='request.POST')
        if form.is_valid():
            apartment = form.save()
            apartment_image = ApartmentImage(image=request.POST['image'], apartment=apartment)
            apartment_image.save()
            return redirect('home')

    else:
        form = HusnaediCreateForm()
    return render(request, 'hus/nytt_husnaedi.html', {
        'form': form
    })

def delete_apartment(request, id):
    apartment = get_object_or_404(Apartment, id=pk)
    apartment.delte()
    return redirect('home')


def um_okkur(request):
    return render(request, 'um_okkur/um_okkur.html', {"title": "Um okkur"})

def starfsmenn(request):
    return render(request, 'starfsmenn/starfsmenn.html', {"title": "Starfsmenn"})

def soluskra(request):
    return render(request, 'soluskra/soluskra.html', {"title": "Söluskrá"})
