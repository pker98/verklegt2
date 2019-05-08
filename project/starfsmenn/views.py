from django.shortcuts import render

def starfsmenn(request):
    return render(request, 'starfsmenn/starfsmenn.html', {"title": "Starfsmenn"})