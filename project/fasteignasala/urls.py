from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="fasteignasala-home"),
    path('um_okkur', views.um_okkur, name="fasteignasala-um_okkur"),
]