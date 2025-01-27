# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Fruta(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    cantidad_disponible = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    fecha = models.DateField()
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('completado', 'Completado')])
    total = models.DecimalField(max_digits=8, decimal_places=2)
    frutas = models.ManyToManyField(Fruta, through='PedidoDetalle')
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)

    def __str__(self):
        return f"Pedido #{self.id} - {self.estado}"


class PedidoDetalle(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    fruta = models.ForeignKey(Fruta, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} de {self.fruta} en {self.pedido}"


class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username


class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return self.nombre


class ClienteVIP(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    nivel_descuento = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    beneficios = models.TextField()

    def __str__(self):
        return f"Cliente VIP: {self.cliente}"


class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    instrucciones = models.TextField()
    frutas = models.ManyToManyField(Fruta)

    def __str__(self):
        return self.nombre


class Venta(models.Model):
    fecha = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venta #{self.id} - {self.total}€"


class HistorialVentas(models.Model):
    fecha = models.DateField()
    total_vendido = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50, choices=[('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta')])
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ventas = models.ManyToManyField(Venta, related_name='historiales')

    def __str__(self):
        return f"Historial del {self.fecha} - {self.total_vendido}€"
