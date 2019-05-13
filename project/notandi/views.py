from django.shortcuts import render, redirect
# from fasteignasala.models import Base_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from notandi.models import Profile
from notandi.forms.profile_form import Profile_form


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

def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = Profile_form(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('minar_sidur')
    context = {'form': Profile_form(instance=profile)}
    return render(request, 'notandi/profile.html', context)
