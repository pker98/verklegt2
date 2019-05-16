import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from fasteignasala.forms.husnaediform import HusnaediCreateForm, HusnaediUpdateForm
from fasteignasala.models import Apartment, ApartmentImage
from django.template import loader, RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from history.models import History
import datetime
from notandi.models import ProfileImage

def find_apartment(request):
    search_filter = request.GET.get('search_filter')
    min_mkr = request.GET.get('min_mkr')
    max_mkr = request.GET.get('max_mkr')
    min_size = request.GET.get('min_size')
    max_size = request.GET.get('max_size')
    min_rooms = request.GET.get('min_rooms')
    max_rooms = request.GET.get('max_rooms')
    zip_values = request.GET.get('zip_list')
    zip_list = zip_values.split(",")
    type_values = request.GET.get('type_list')
    type_list = type_values.split(",")
    for i in range(len(type_list)):
        if type_list[i] == '1':
            type_list[i] = "Einbýlishús"
        if type_list[i] == '2':
            type_list[i] = "Tvíbýlishús"
        if type_list[i] == '3':
            type_list[i] = "Fjölbýlishús"
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
        'first_image': x.apartmentimage_set.first().image,
    } for x in Apartment.objects.filter(address__icontains=search_filter).
        filter(price__gte=min_mkr, price__lte=max_mkr).
        filter(num_rooms__gte=min_rooms, num_rooms__lte=max_rooms).
        filter(size__gte=min_size, size__lte=max_size).
        filter(zip__in=zip_list).filter(type__in=type_list)]

    return apartments

def home(request, query=None):
    if 'search_filter' in request.GET:
        apartments = find_apartment(request)
        return JsonResponse({'data': apartments})
    context = {"apartments" : Apartment.objects.all(), 'title' : 'LúxHús'}
    return render(request, 'forsida/home.html', context)

def soluskra(request, query=None):
    if 'search_filter' in request.GET:
        apartments = find_apartment(request)
        return JsonResponse({'data': apartments})
    context = {"apartments": Apartment.objects.all(), 'title' : 'Söluskrá'}
    return render(request, 'soluskra/soluskra.html', context)


def get_apartm_by_id(request, id):
    if request.method == "GET" and request.user.is_authenticated:
        get_object_or_404(Apartment, pk=id)
        try:
            old_history = History.objects.get(user_id=request.user.id, apartment_id=id)
            old_history.viewed_on = datetime.datetime.now()
            old_history.save()
        except History.DoesNotExist:
            new_history = History(user_id=request.user.id, apartment_id=id)
            new_history.save()
    apartment = get_object_or_404(Apartment, pk=id)
    format_price = format(apartment.price,',d').replace(",",".")
    return render(request, 'hus/husnaedi_details.html', {

    'apartment': get_object_or_404(Apartment, pk=id), 'price' : format_price,
     'profiles' : ProfileImage.objects.all()
    })


@login_required
@permission_required('apartment.can_add_appartment', raise_exception=True)
def create_apartment(request):
    if request.method == 'POST':
        form = HusnaediCreateForm(data=request.POST)
        if form.is_valid():

            apartment = form.save()
            apartment.seller = request.user
            apartment.save()
            apartment_image = ApartmentImage(image=request.POST['image'], apartment=apartment)
            apartment_image.save()
            return redirect('fasteignasala-home')
    else:
        form = HusnaediCreateForm()
    return render(request, 'hus/nytt_husnaedi.html', {
        'form': form
    })

@login_required
@permission_required('apartment.can_delete_appartment', raise_exception=True)
def delete_apartment(request, id):
    apartment = get_object_or_404(Apartment, pk=id)
    apartment.delete()
    return redirect(reverse('fasteignasala-home'))

@login_required
@permission_required('apartment.can_change_appartment', raise_exception=True)
def update_apartment(request, id):
    instance = get_object_or_404(Apartment, pk=id)
    if request.method == 'POST':
        form = HusnaediUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('apartment_details', id=id)
    else:
        form = HusnaediUpdateForm(instance=instance)
    return render(request, 'hus/breyta_husnaedi.html', {
        'form': form,
        'id': id
    })

def um_okkur(request):
    return render(request, 'um_okkur/um_okkur.html', {"title": "Um okkur"})

def starfsmenn(request):
    users = User.objects.filter(is_staff=True)
    context = {
        'users': users,
        'title': "Starfsmenn",
        'profiles': ProfileImage.objects.all()
    }
    return render(request, 'starfsmenn/starfsmenn.html', context)
