from django.contrib import admin
from .models import Proveedor, Categoria, Fruta, Cliente, Empleado, Pedido, PedidoDetalle, Receta, Venta, HistorialVentas, ClienteVIP

# Registra los modelos en el admin
admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Fruta)
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Pedido)
admin.site.register(PedidoDetalle)
admin.site.register(Receta)
admin.site.register(Venta)
admin.site.register(HistorialVentas)
admin.site.register(ClienteVIP)
