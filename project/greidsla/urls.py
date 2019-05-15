from django.urls import path
from . import views

urlpatterns = [
    path('greidsluferli/<int:id>', views.greidsla, name='greidsla'),
    path('stadfesting/<int:id>', views.stadfesting, name='stadfesting')
]
