from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_view, name='inicio_login'),
    path('contraseña/', views.contraseña_view, name='contraseña'),
    path('login/', views.contraseña_view, name='login_form'),
]
