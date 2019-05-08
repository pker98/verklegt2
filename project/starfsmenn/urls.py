from django.urls import path
from . import views

urlpatterns = [
    path('', views.starfsmenn, name="starfsmenn-home"),
]