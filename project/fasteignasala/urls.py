from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="fasteignasala-home"),
    path('starfsmenn/', views.starfsmenn, name="starfsmenn-home"),
    path('um_okkur/', views.um_okkur, name="um_okkur-home"),
    path('soluskra/', views.soluskra, name="soluskra-home"),
    path('nyskraning/', views.nyskraning, name="nyskraning"),
]