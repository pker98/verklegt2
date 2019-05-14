from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def greidsla(request):
    return render(request, 'greidsluferli/greidsluferli.html', {"title": "Greiðsluferli"})

@login_required
def kaupsamningur(request):
    return render(request, 'greidsluferli/kaupsamningur.html', {"title": "Kaupsamningur"})