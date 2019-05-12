from django.shortcuts import render, redirect
# from fasteignasala.models import Base_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView


def nyskraning(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('innskraning')
    form = UserCreationForm()
    context = {'form': form, 'title': 'Nýskráning'}
    return render(request, 'notandi/nyskraning.html', context)

def innskraning(request):
    form = LoginView()

    context = {'form': form, 'title': 'Innskráning'}
    return render(request, 'notandi/innskraning.html', context)
