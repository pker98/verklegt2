from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from fasteignasala.models import Apartment
from greidsla.forms.greidsluform import GreidsluferliForm
from greidsla.models import Buyer

@login_required
def greidsla(request, id):
    if request.method == 'POST':
        payment_form = GreidsluferliForm(data=request.POST)
        if payment_form.is_valid():
            payment_form.save()
            return redirect('yfirlit', id=id)
    else:
        payment_form = GreidsluferliForm()
    context = {'payment_form': payment_form, 'id': id}
    return render(request, 'greidsluferli/greidsluupplysingar.html', context)

@login_required
def yfirlit(request, id):
    apartment = get_object_or_404(Apartment, pk=id)
    buyer_info = get_object_or_404(Buyer, pk=request.user.id)
    context = { 'apartment': apartment}
    return render(request, 'greidsluferli/greidsluferliyfirlit.html'. context)

@login_required
def stadfesting(request, id):
    apartment = get_object_or_404(Apartment, pk=id)
    context = { 'apartment': apartment}
    return render(request, 'greidsluferli/greidslustadfesting.html', context)