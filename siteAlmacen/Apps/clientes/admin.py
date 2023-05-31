from django.contrib import admin
from Apps.clientes.models import Cliente
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    # readonly_fields = ('correoCliente',) #No permite edicion de create y update
    # readonly_fields = ('created', 'updated') #No permite edicion de create y update
    list_display = ('nombreCliente', 'direccionCliente', 'telefonoCliente', 'correoCliente')
    # ordering = ('nombreCliente', 'direccionCliente', 'correoCliente')  
    # En caso que sea una sola ordering('column',)
    #form de busqueda
    search_fields = ('nombreCliente','correoCliente') 
    #Campo relacionado

    list_filter = ('nombreCliente', 'correoCliente','direccionCliente') 
    # Campos relacionados

admin.site.register(Cliente, ClienteAdmin)