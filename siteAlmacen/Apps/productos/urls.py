from django.urls import path
from Apps.productos.views import home
from Apps.productos.views import ProductoView

app_name = "productos"
urlpatterns = [
    path('inicio/', home, name= 'home'),
    path('', ProductoView.as_view()),
]
