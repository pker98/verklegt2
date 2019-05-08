from django.shortcuts import render

def nyskraning(request):
    return render(request, 'nyskraning/nyskraning.html', {'title':'Nýskráning'})
