from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
# from fasteignasala.forms.husnaediform import HusnaediCreateForm, HusnaediUpdateForm
from fasteignasala.models import Apartment, ApartmentImage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

def home(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        apartments = [{
            'id': x.id,
            'address': x.address,
            'price': x.price,
            'fire_insurance': x.fire_insurance,
            'estimated_value': x.estimated_value,
            'type': x.type,
            'size': x.size,
            'num_rooms': x.num_rooms,
            'num_bed_room': x.num_bed_room,
            'num_bath_room': x.num_bath_room,
            'description': x.description,
            'town': x.town,
            'zip': x.zip,
            'first_image': x.apartmentimage_set.first().image
        } for x in Apartment.objects.filter(address__icontains=search_filter).order_by('address')]
        return JsonResponse({ 'data': apartments })
    context = {"apartments" : Apartment.objects.all().order_by('address')}
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

    #else:
        form = HusnaediCreateForm()
    return render(request, 'hus/nytt_husnaedi.html', {
        'form': form
    })

def delete_apartment(request, id):
    apartment = get_object_or_404(Apartment, pk=id)
    apartment.delete()
    return redirect('home')

def update_apartment(request, id):
    instance = get_object_or_404(Apartment, pk=id)
    if request.method == 'POST':
        form = HusnaediUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('husnaedi_details', id=id)
    else:
        form = HusnaediUpdateForm(instance=instance)
    return render(request, 'hus/breyta_husnaedi.html', {
        'form': form,
        'id': id
    })

def um_okkur(request):
    return render(request, 'um_okkur/um_okkur.html', {"title": "Um okkur"})

def starfsmenn(request):
    return render(request, 'starfsmenn/starfsmenn.html', {"title": "Starfsmenn"})

def soluskra(request):
    return render(request, 'soluskra/soluskra.html', {"title": "Söluskrá"})
