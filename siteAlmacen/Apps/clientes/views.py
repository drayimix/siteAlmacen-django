from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status, mixins


from Apps.clientes.models import Cliente
from Apps.clientes.serializers import ClienteSerializer

# Create your views here.
def home(request):
    return HttpResponse("Bienvenidos- clientes")

# class ClienteList(generics.ListCreateAPIView):
#     queryset=Cliente.objects.all()
#     serializer_class=ClienteSerializer

# class ClienteList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     """
#     Lista Clientes
#     """
#     queryset=Cliente.objects.all()
#     serializer_class=ClienteSerializer 

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
 

# class clienteDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Cliente.objects.all()
#     serializer_class=ClienteSerializer

# class ClienteDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset=Cliente.objects.all()
#     serializer_class=ClienteSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request,*args,**kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request,*args,**kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request,*args,**kwargs)

class ClienteList(APIView):
    """
    Lista Clientes
    """
    def get(self, request, format=None):
        clientes = Cliente.objects.all()
        data = {"results": list(clientes.values("nombreCliente", "direccionCliente", "telefonoCliente", "correoCliente", "passwordCliente"))}
        print(data)
        serializer= ClienteSerializer(clientes, many=True)
        return Response({"clientes":serializer.data})
    
    def post(self, request, format=None):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClienteDetail(APIView):
    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404
    
    def get(self, request,pk, format=None):
        cliente= self.get_object(pk)
        serializer = ClienteSerializer(cliente)
        return Response({"cliente": serializer.data})
    
    def put(self, request,pk , format=None):
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk, format=None):
        cliente = self.get_object(pk)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)