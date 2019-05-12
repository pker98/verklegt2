from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('nyskraning/', views.nyskraning, name="nyskraning"),
    path('innskraning/', auth_views.LoginView.as_view(template_name='notandi/innskraning.html'), name="innskraning"),
    path('utskraning/', auth_views.LogoutView.as_view(next_page='innskraning'), name="utskraning"),
]