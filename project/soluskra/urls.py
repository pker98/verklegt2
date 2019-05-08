from django.urls import path
from . import views

urlpatterns = [
    path('', views.soluskra, name="soluskra-home"),
]