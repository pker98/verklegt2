from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from fasteignasala.models import Apartment
from greidsla.forms.greidsluform import GreidsluferliForm

def send_get_form(form=None):
    if form:
        temp_form = form
    else:
        return temp_form


@login_required
def greidsla(request, id):
    if request.method == 'POST':
        payment_form = GreidsluferliForm(data=request.POST)
        send_get_form(payment_form)
        return redirect('yfirlit', id=id)
    else:
        payment_form = GreidsluferliForm()
    context = {'payment_form': payment_form, 'id': id}
    return render(request, 'greidsluferli/greidsluupplysingar.html', context)

@login_required
def yfirlit(request, id):
    apartment = get_object_or_404(Apartment, pk=id)
    umsyslugjald = apartment.price * 0.8
    total = apartment.price + 17500 + umsyslugjald + 2500
    context = { 'apartment': apartment,
                'special_price': umsyslugjald, 'total': total}
    return render(request, 'greidsluferli/greidsluferliyfirlit.html', context)

@login_required
def stadfesting(request, id):
    apartment = get_object_or_404(Apartment, pk=id)
    context = { 'apartment': apartment}
    return render(request, 'greidsluferli/greidslustadfesting.html', context)