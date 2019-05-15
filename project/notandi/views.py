from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from notandi.models import Profile
from notandi.forms.profileform import ProfileForm
from .forms.profileform import RegistrationForm
from history.models import History


def nyskraning(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('innskraning')
    form = RegistrationForm()
    context = {'form': form, 'title': 'Nýskráning'}
    return render(request, 'notandi/nyskraning.html', context)


def innskraning(request):
    form = LoginView()
    context = {'form': form, 'title': 'Innskráning'}
    return render(request, 'notandi/innskraning.html', context)


def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    #user = User.objects.filter(user=request.user).first()#Not sure if I add user here
    history_list = History.objects.filter(user_id=request.user.id).order_by('-viewed_on')[:10]
    if request.method == "POST":
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('minar_sidur')
    context = {'form': ProfileForm(instance=profile), 'history' : history_list, 'profile' : profile}
    return render(request, 'notandi/profile.html', context)
