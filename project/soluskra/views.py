from django.shortcuts import render

def soluskra(request):
    return render(request, 'soluskra/soluskra.html', {"title": "Söluskrá"})