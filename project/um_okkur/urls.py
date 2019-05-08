from django.urls import path
from . import views

urlpatterns = [
    path('', views.um_okkur, name="um_okkur-home"),
]