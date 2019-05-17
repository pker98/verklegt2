from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from fasteignasala.models import Apartment
from greidsla.forms.greidsluform import GreidsluferliForm
from greidsla.models import Buyer
from django.contrib.auth.models import User


@login_required
def greidsla(request, id):
    if request.method == "POST":
        form = GreidsluferliForm(data=request.POST)
        if form.is_valid():
            buyer = form.save()
            buyer.user_id_id = request.user.id
            buyer.save()
            return redirect('yfirlit', id)
    else:
        form = GreidsluferliForm()
    context = {'payment_form': form, 'id': id, 'title': 'Yfirlit'}
    return render(request, 'greidsluferli/greidsluupplysingar.html', context)


@login_required
def yfirlit(request, id):
    buyer = Buyer.objects.filter(user_id=request.user.id).first()
    apartment = get_object_or_404(Apartment, pk=id)
    umsyslugjald = apartment.price * 0.08
    total = apartment.price + 17500 + umsyslugjald + 2500
    context = { 'apartment': apartment,
                'special_price': umsyslugjald, 'total': total,
                'buyer' : buyer,
                'id': id}

    return render(request, 'greidsluferli/greidsluferliyfirlit.html', context)


@login_required
def stadfesting(request, id):
    apartment = get_object_or_404(Apartment, pk=id)
    apartment.delete()
    context = { 'apartment': apartment }
    return render(request, 'greidsluferli/greidslustadfesting.html', context)