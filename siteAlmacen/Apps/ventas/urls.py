from django.urls import path
from Apps.ventas.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]