from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from notandi.models import ProfileImage
from notandi.forms.profileform import ProfileImageForm, UserUpdateForm
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
    #profile = Profile.objects.filter(user=request.user).first()#Not sure if I add user here
    user = User.objects.filter(id=request.user.id).first()
    profile = ProfileImage.objects.filter(user_id=request.user.id).first()
    history_list = History.objects.filter(user_id=request.user.id).order_by('-viewed_on')[:10]
    if request.method == "POST":
        image_form = ProfileImageForm(instance=profile, data=request.POST)
        form = UserUpdateForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
            image_form.save()
            return redirect('minar_sidur')
    context = {'form': UserUpdateForm(instance=user), 'image_form': ProfileImageForm(instance=profile),
               'history': history_list, 'user': user, 'profile': profile}
    return render(request, 'notandi/profile.html', context)
