from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def greidsla(request):
    return render(request, 'greidsluferli/greidsluferli.html', {"title": "Greiðsluferli"})

@login_required
def almupp(request):
    return render(request, 'greidsluferli/upplysingar.html', {"title": "Almennar Upplýsingar"})

@login_required
def stadfesting(request):
    return render(request, 'greidsluferli/stadfesting.html', {"title": "Staðfesting"})