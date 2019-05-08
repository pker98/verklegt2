from django.shortcuts import render

def um_okkur(request):
    return render(request, 'um_okkur/um_okkur.html', {"title": "Um okkur"})