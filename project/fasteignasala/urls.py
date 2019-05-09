from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="fasteignasala-home"),
    path('starfsmenn/', views.starfsmenn, name="starfsmenn-home"),
    path('um_okkur/', views.um_okkur, name="um_okkur-home"),
    path('soluskra/', views.soluskra, name="soluskra-home"),
    path('nyskraning/', views.nyskraning, name="nyskraning"),
    path('innskraning/', auth_views.LoginView.as_view(template_name='innskraning/innskraning.html'), name="innskraning"),
    path('utskraning/', auth_views.LogoutView.as_view(), name="utskraning"),
]