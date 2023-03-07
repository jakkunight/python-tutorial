#/usr/bin/python
# ANTES DE EMPEZAR:
# Vamos a aprender sobre el uso de Git y GitHub para tener un "control de versiones" de
# nuestro código. También vamos a planificar la solución de manera que sea más fácil usar
# las herramientas.
#
# Problema del supermercado.
# Supongamos que contamos con una lista de productos, con sus precios y existencias.
# También contamos con otra lista (puede estar inicialmente vacía) de clientes.
# Por supuesto, tenemos con una nómina de empleados que operan el negocio.
# Hacer un programa que permita agregar, modificar y eliminar elementos de nuestras listas
# y mostrarlos en pantalla.
# 
# No hace falta usar una Base de Datos para este caso, pero de todos modos vamos a crear un
# software que les permita conocer lo básico acerca de como usar los datos provenientes de 
# la misma.
# SPOILER: Vamos a ver como conectarnos a una Base de Datos SQL desde Python si todo sale bien.
# 
# Desafío secreto: Implementar un sistema para gestionar nuestro "supermercado".

# Creamos diccionarios para modelar nuestros datos:
Producto = {
    "id": 0,
    "nombre": "",
    "descripcion": "",
    "coste": 0,
    "precio": 0,
    "cantidad": 0
}
Cliente = {
    "id": 0,
    "nombre": "",
    "ruc": ""
}
Empleado = {
    "id": 0,
    "nombre": "",
    "password": "",
    "email": "",
    "ci": "",
    "cargo": ""
}

# Creamos una lista con los diversos cargos del sistema:
Cargos = [
    "Programador",
    "Vendedor",
    "Encargado de Stock",
    "Auditor",
    "Supervisor de Ventas",
    "Ejecutivo en Jefe",
    "Contador",
    "Administrador",
    "Aprendiz"
]

# Creamos nuestras tablas de datos:
base_de_datos = {
    "productos": [],
    "clientes": [],
    "empleados": []
}

# Creamos rutinas para gestionar cada lista.
def insertar(lista, item):
    item["id"] = len(base_de_datos[lista])
    base_de_datos[lista].append(item)

def leer(lista, campo, valor):
    if(not campo or not valor):
        return base_de_datos[lista]
    datos = []
    for item in base_de_datos[lista]:
        if(item[campo] == valor):
            datos.append(item)
    return datos

def editar(lista, nuevo_dato, _id):
    base_de_datos[lista][_id] = nuevo_dato

def borrar(lista, _id):
    base_de_datos[lista].pop(_id)
    for i in range(0, len(base_de_datos[lista])):
        base_de_datos[lista][i]["id"] = i

# Ahora creamos rutinas para crear registros de forma concreta, pues no debemos
# modificar los modelos de datos originales:
def crear_producto(nombre, descripcion = "No disponible", coste = 0, precio = 0, cantidad = 1):
    if(not nombre or coste < 0 or precio < 0 or cantidad < 0):
        return False
    temp = Producto.copy()
    temp["nombre"] = nombre
    temp["descripcion"] = descripcion
    temp["coste"] = coste
    temp["cantidad"] = cantidad
    return temp

def crear_cliente(nombre, ruc):
    if(not nombre or not ruc):
        return False
    temp = Cliente.copy()
    temp["nombre"] = nombre
    temp["ruc"] = ruc
    return temp

def crear_empleado(nombre, password, ci, cargo, email = "No disponible"):
    if(not nombre or not password or not ci or not cargo):
        return False
    temp = Empleado.copy()
    temp["nombre"] = nombre
    temp["password"] = password
    temp["email"] = email
    temp["ci"] = ci
    # Validamos el cargo:
    if(cargo in Cargos):
        temp["cargo"] = cargo
    else:
        temp["cargo"] = "Aprendiz"
    return temp

# Creamos una función de login sencilla para poder cargar los datos
def login():
    print("=========")
    print("| LOGIN |")
    print("=========")
    input("Nombre: ")
    input("Password: ")

# Creamos las rutinas correspondientes a la interfaz de usuario:

    
