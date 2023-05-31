from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from Apps.productos.models import Producto, TipoProducto

# Create your views here.
def home(request):
    return HttpResponse("Bienvenidos-productos")

class ProductoView(APIView):
    def get(self, request):
        productos = Producto.objects.all()
        return Response({"productos": productos})