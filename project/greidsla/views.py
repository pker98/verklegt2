from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from fasteignasala.models import Apartment
from history.models import History
from notandi.models import Profile


@login_required
def greidsla(request, id):
    apartment = get_object_or_404(Apartment, pk=id)
    context = { 'apartment': apartment}
    return render(request, 'greidsluferli/greidsluferli.html', context)

@login_required
def stadfesting(request, id):
    profile = Profile.objects.filter(user=request.user)
    apartment = get_object_or_404(Apartment, pk=id)
    context = { 'profile': profile, 'apartment': apartment}
    return render(request, 'greidsluferli/stadfesting.html', context)