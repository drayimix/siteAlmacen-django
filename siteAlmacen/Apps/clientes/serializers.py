from dataclasses import field
from statistics import mode

from rest_framework import serializers
from Apps.clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

def validate_nombreCliente(self, value):
    if len(value) < 3:
        raise serializers.ValidationError('Nombre no puede ser tan corto')
    else:
        return value
    
def validate_passwordCliente(self, value):
    if len(value)<8:
        raise serializers.ValidationError('El password debe tner mas de 8 caracteres')
    else:
        return value