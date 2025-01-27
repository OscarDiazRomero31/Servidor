# Servidor
Proyecto de la asignatura de Servidor (Django).

# Lanzar Proyecto ya Creado
Descargar proyecto con GIT
sudo apt-get install python3-venv  -> Sino está instalado ya
No situamos en la carpeta 2daw
python3 -m venv myvenv -> Creamos el entorno
source myvenv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate -> Creamos base de datos
python manage.py runserver 0.0.0.0:8080 -> Lanzamos el servidor

# Modelo ER
Esquema inicial:
Proveedor tiene una relación OneToMany con Fruta (un proveedor puede suministrar varias frutas).
Categoria tiene una relación OneToMany con Fruta (una categoría puede tener varias frutas).
Fruta tiene una relación ManyToMany con Pedido a través de PedidoDetalle (un pedido puede contener varias frutas y viceversa).
Cliente tiene una relación OneToOne con el modelo de usuario de Django (auth.User).
ClienteVIP tiene una relación OneToOne con Cliente.
Pedido tiene una relación ManyToOne con Cliente (un cliente puede tener varios pedidos).
Venta tiene una relación ManyToOne con Cliente y Empleado.
HistorialVentas tiene una relación ManyToMany con Venta (varias ventas pueden agruparse en un historial).
Receta tiene una relación ManyToMany con Fruta (una receta puede usar varias frutas).

