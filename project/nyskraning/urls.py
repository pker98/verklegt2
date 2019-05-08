from django.urls import path
from . import views

urlpatterns = [
    path('', views.nyskraning, name="nyskraning"),
]