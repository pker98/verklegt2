from django.shortcuts import render


def greidsla(request):
    return render(request, 'greidsluferli/greidsla.html', {"title": "Greiðsluferli"})

