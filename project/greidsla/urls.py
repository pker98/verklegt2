from django.urls import path
from . import views

urlpatterns = [
    path('greidsluferli/', views.greidsla, name='greidsla'),
    path('almennar_upplysingar/', views.almupp, name='upplysingar')
]
