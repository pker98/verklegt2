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

    if request.method == 'GET':
        form = GreidsluferliForm(data=request.GET)
        if form.is_valid():
            return redirect('yfirlit')
    else:
        form = GreidsluferliForm()
    context = {'payment_form': form, 'id': id}
    return render(request, 'greidsluferli/greidsluupplysingar.html', context)

@login_required
def yfirlit(request, id):
    data = 1
    apartment = get_object_or_404(Apartment, pk=id)
    umsyslugjald = apartment.price * 0.8
    total = apartment.price + 17500 + umsyslugjald + 2500
    context = { 'apartment': apartment,
                'special_price': umsyslugjald, 'total': total,
                'data': data}

    return render(request, 'greidsluferli/greidsluferliyfirlit.html', context)

@login_required
def stadfesting(request, id):
    apartment = get_object_or_404(Apartment, pk=id)
    context = { 'apartment': apartment}
    return render(request, 'greidsluferli/greidslustadfesting.html', context)