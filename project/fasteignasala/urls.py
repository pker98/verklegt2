from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="fasteignasala-home"),
    path('starfsmenn/', views.starfsmenn, name="starfsmenn-home"),
    path('um_okkur/', views.um_okkur, name="um_okkur-home"),
    path('soluskra/', views.soluskra, name="soluskra-home"),
    path('notandi/', include('notandi.urls')),
    path('<int:id>', views.get_apartm_by_id, name='apartment_details'),
    path('nytt_husnaedi/', views.create_apartment, name='nytt_husnaedi'),
    path('eyda_husnaedi/<int:id>', views.delete_apartment, name='eyda_husnaedi')
]