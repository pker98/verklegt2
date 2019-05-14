from django.urls import path
from . import views

urlpatterns = [
    path('greidsluferli/', views.greidsla, name='greidsla'),
    path('kaupsamningur/', views.kaupsamningur, name='kaupsamningur')
]
