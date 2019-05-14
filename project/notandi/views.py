from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from notandi.models import Profile
from notandi.forms.profile_form import Profile_form
from .forms.profile_form import RegistrationForm
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
    history_list = History.objects.filter(user_id=request.user.id)
    if request.method == "POST":
        form = Profile_form(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('minar_sidur')
    context = {'form': Profile_form(instance=profile), 'history' : history_list}
    return render(request, 'notandi/profile.html', context)
