from django.urls import path
from Apps.clientes.views import home, ClienteDetail, ClienteList


app_name = "clientes"
urlpatterns = [
    path('inicio/', home, name= 'home'),
    path('', ClienteList.as_view()),
    path('<int:pk>', ClienteDetail.as_view())
]