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
# Podríamos guardar las contraseñas en texto plano y no habría problemas si estamos
# en un entorno de pruebas.
# En producción, en cambio, SIEMPRE debemos cifrar las contraseñas a guardar en una
# base de datos. ¡SIEMPRE!
# En Europa, y en muchos otros países, es un crimen guardar contraseñas sin encriptar 
# en entornos de producción.
# Para ello vamos a usar un módulo de Python llamado argon2-cffi.
# Como es un módulo externo, habrá que instalarlo mediante pip antes de ejecutar
# nuestro código.
# 
# Desafío secreto: Implementar un sistema para gestionar nuestro "supermercado".

# Importamos el password hasher:
import argon2
ph = argon2.PasswordHasher()

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
def insertar(lista = False, item = False):
    if(not lista or not item):
        return False
    global base_de_datos
    item["id"] = len(base_de_datos[lista])
    base_de_datos[lista].append(item)
    return True

def leer(lista = False, campo = False, valor = False):
    if(not lista):
        return False
    global base_de_datos
    if(not campo or not valor):
        return base_de_datos[lista]
    datos = []
    for item in base_de_datos[lista]:
        if(item[campo] == valor):
            datos.append(item)
    return datos

def editar(lista = False, nuevo_dato = False, _id = False):
    if(not lista or not nuevo_dato):
        print("[ERROR] No hay nada que editar.")
        input("Presione ENTER para continuar...")
        return False
    if(_id != 0 and not _id):
        print("[ERROR] No hay ID.")
        input("Presione ENTER para continuar...")
        return False
    global base_de_datos
    base_de_datos[lista][_id] = nuevo_dato
    return True

def borrar(lista = False, _id = False):
    if(not lista or not _id):
        return False
    global base_de_datos
    base_de_datos[lista].pop(_id)
    for i in range(0, len(base_de_datos[lista])):
        base_de_datos[lista][i]["id"] = i
    return True

# Ahora creamos rutinas para crear registros de forma concreta, pues no debemos
# modificar los modelos de datos originales:
def crear_producto(nombre = False, descripcion = "No disponible", coste = 0, precio = 0, cantidad = 1):
    if(not nombre or coste < 0 or precio < 0 or cantidad < 0):
        return False
    global Producto
    temp = Producto.copy()
    temp["nombre"] = nombre
    temp["descripcion"] = descripcion
    temp["coste"] = coste
    temp["precio"] = precio
    temp["cantidad"] = cantidad
    return temp

def crear_cliente(nombre = False, ruc = False):
    if(not nombre or not ruc):
        print("[ERROR] No hay datos.")
        input("Presione ENTER para continuar...")
        return False
    global Cliente
    temp = Cliente.copy()
    temp["nombre"] = nombre
    temp["ruc"] = ruc
    return temp

def crear_empleado(
    nombre = False,
    password = False,
    ci = False,
    cargo = False,
    email = "No disponible"
):
    if(not nombre or not password or not ci or not cargo):
        return False
    global ph, Clientes, Empleado
    temp = Empleado.copy()
    temp["nombre"] = nombre
    # Encriptamos la contraseña para guardarla:
    hash = ph.hash(password)
    while(ph.check_needs_rehash(hash)):
        hash = ph.hash(password)
    temp["password"] = hash
    temp["email"] = email
    temp["ci"] = ci
    # Validamos el cargo:
    if(cargo in Cargos):
        temp["cargo"] = cargo
    else:
        temp["cargo"] = "Aprendiz"
    return temp


# Creamos las rutinas correspondientes a la interfaz de usuario:
def pause_exit():
    print("Hasta la proxima!")
    input("Presione ENTER para continuar...")
    exit(0)

def clear():
    print("\033[2J", end="")
    print("\033[0;0f", end="")

# Creamos una función de login sencilla para poder cargar los datos
def login():
    clear()
    global ph
    print("=========")
    print("| LOGIN |")
    print("=========")
    usuario = input("Nombre: ")
    # Para las contraseñas vamos a usar un módulo de Python llamado getpass,
    # el cual nos permite leer datos sin hacerles un "eco" en la pantalla como input():
    from getpass import getpass
    password = getpass("Password: ")
    for registro in leer("empleados"):
        if(registro["nombre"] != usuario):
            continue
        return ph.verify(registro["password"], password)

# Sección de Productos:
def menu_consultar_productos():
    while(True):
        clear()
        print("-----------------------------------")
        print("| SUPERMERCADOS SAN PABLO - STOCK |")
        print("-----------------------------------")
        print(" ")
        print("OPCIONES:")
        print(" ")
        print("    1) MOSTRAR LISTA DE PRODUCTOS")
        print("    2) BUSCAR PRODUCTO")
        print("    0) VOLVER ATRAS")
        print(" ")
        opcion = int(input("Ingrese una opcion valida: "))
        if(opcion == 0):
            break

        if(opcion == 1):
            datos = leer("productos")
            for item in datos:
                keys = list(item.keys())
                valores = list(item.values())
                print("{")
                for i in range(0, len(keys)):
                    print("    " + keys[i] + ": " + str(valores[i]))
                print("}")
                input("Presione ENTER para ver el siguiente producto...")
                
        if(opcion == 2):
            p = input("Ingrese el parametro de busqueda: ")
            v = input("Ingrease el valor del parametro a buscar: ")
            datos = leer("productos", p, v)
            for item in datos:
                keys = list(item.keys())
                valores = list(item.values())
                print("{")
                for i in range(0, len(keys)):
                    print("    " + keys[i] + ": " + str(valores[i]))
                print("}")
                input("Presione ENTER para ver el siguiente producto...")


def insertar_producto():
    while(True):
        clear()
        print("-----------------------------------")
        print("| SUPERMERCADOS SAN PABLO - STOCK |")
        print("-----------------------------------")
        print(" ")
        print("    NUEVO PRODUCTO:")
        print(" ")
        nombre = input("Intruduzca nombre del producto: ")
        descripcion = input("Introduzca descripcion: ")
        coste = int(input("Introduzca coste de adquisicion: "))
        precio = int(input("Introduzca precio de venta: "))
        cantidad = int(input("Introduzca cantidad: "))
        temp = crear_producto(nombre, descripcion, coste, precio, cantidad)
        if(not temp):
            input("[ERROR] Presione ENTER para reingresar los datos...")
            continue
        estado = insertar("productos", temp)
        if(estado):
            input("[EXITO] Presione ENTER para continuar...")
            break
        else:
            input("[ERROR] Presione ENTER para reintentar...")


def editar_producto():
    while(True):
        clear()
        print("-----------------------------------")
        print("| SUPERMERCADOS SAN PABLO - STOCK |")
        print("-----------------------------------")
        print(" ")
        p = input("Ingrese el parametro de busqueda: ")
        v = input("Ingrease el valor del parametro a buscar: ")
        datos = leer("productos", p, v)
        if(not datos):
            input("[ERROR] Presione ENTER para reingresar los datos...")
            continue
        print("    DATOS DEL PRODUCTO:")
        for item in datos:
            keys = list(item.keys())
            valores = list(item.values())
            for i in range(0, len(keys)):
                print("        " + keys[i] + ": " + str(valores[i]))
        nombre = input("Intruduzca nombre del producto: ")
        if(nombre == "" or not nombre):
            nombre = datos[0]["nombre"]
        descripcion = input("Introduzca descripcion: ")
        if(descripcion == "" or not descripcion):
            descripcion = datos[0]["descripcion"]
        coste = int(input("Introduzca coste de adquisicion: "))
        if(coste == "" or not coste):
            coste = datos[0]["coste"]
        else:
            coste = int(coste)
        precio = int(input("Introduzca precio de venta: "))
        if(precio == "" or not precio):
            precio = datos[0]["precio"]
        else:
            precio = int(precio)
        cantidad = input("Introduzca cantidad: ")
        if(cantidad == "" or not cantidad):
            cantidad = datos[0]["cantidad"]
        else:
            cantidad = int(cantidad)
        temp = crear_producto(nombre, descripcion, coste, precio, cantidad)
        if(not temp):
            input("[ERROR] Presione ENTER para reingresar los datos...")
            continue
        estado = editar("productos", temp, item["id"])
        if(estado == True):
            input("[EXITO] Presione ENTER para continuar...")
            break
        else:
            input("[ERROR] Presione ENTER para continuar...")
            break

def eliminar_producto():
    while(True):
        clear()
        print("-----------------------------------")
        print("| SUPERMERCADOS SAN PABLO - STOCK |")
        print("-----------------------------------")
        print(" ")
        id = int(input("Ingrese el ID del producto a eliminar: "))
        check = input("Esta seguro de que desea eliminar el producto? [y/N]: ")
        if(check.upper() == "Y"):
            estado = borrar("productos", id)
            if(estado):
                input("[EXITO] Presione ENTER para continuar...")
                break
            else:
                input("[ERROR] Presione ENTER para reintentar...")
        else:
            print("El usuario ha cancelado la operacion.")
            input("[EXITO] Presione ENTER para continuar...")
            break


def menu_productos():
    while(True):
        clear()
        print("-----------------------------------")
        print("| SUPERMERCADOS SAN PABLO - STOCK |")
        print("-----------------------------------")
        print(" ")
        print("OPCIONES:")
        print(" ")
        print("    1) CONSULTAR INVENTARIO")
        print("    2) INSERTAR PRODUCTO")
        print("    3) ACTUALIZAR PRODUCTO")
        print("    4) ELIMINAR PRODUCTO")
        print("    0) VOLVER ATRAS")
        print(" ")
        opcion = int(input("Ingrese una opcion valida: "))
        if(opcion == 0):
            break
        if(opcion == 1):
            menu_consultar_productos()
        if(opcion == 2):
            insertar_producto()
        if(opcion == 3):
            editar_producto()
        if(opcion == 4):
            eliminar_producto()


# Sección de Clientes:
def menu_consultar_clientes():
    while(True):
        clear()
        print("--------------------------------------")
        print("| SUPERMERCADOS SAN PABLO - CLIENTES |")
        print("--------------------------------------")
        print(" ")
        print("OPCIONES:")
        print(" ")
        print("    1) MOSTRAR LISTA DE CLIENTES")
        print("    2) BUSCAR CLIENTE")
        print("    0) VOLVER ATRAS")
        print(" ")
        opcion = int(input("Ingrese una opcion valida: "))
        if(opcion == 0):
            break

        if(opcion == 1):
            datos = leer("clientes")
            for item in datos:
                keys = list(item.keys())
                valores = list(item.values())
                print("{")
                for i in range(0, len(keys)):
                    print("    " + keys[i] + ": " + str(valores[i]))
                print("}")
                input("Presione ENTER para ver el siguiente clieinte...")
                
        if(opcion == 2):
            p = input("Ingrese el parametro de busqueda: ")
            v = input("Ingrease el valor del parametro a buscar: ")
            datos = leer("clientes", p, v)
            for item in datos:
                keys = list(item.keys())
                valores = list(item.values())
                print("{")
                for i in range(0, len(keys)):
                    print("    " + keys[i] + ": " + str(valores[i]))
                print("}")
                input("Presione ENTER para ver el siguiente cliente...")


def insertar_cliente():
    while(True):
        clear()
        print("--------------------------------------")
        print("| SUPERMERCADOS SAN PABLO - CLIENTES |")
        print("--------------------------------------")
        print(" ")
        print("    NUEVO PRODUCTO:")
        print(" ")
        nombre = input("Intruduzca nombre del cliente: ")
        ruc = input("Introduzca descripcion: ")
        temp = crear_producto(nombre, ruc)
        if(not temp):
            input("[ERROR] Presione ENTER para reingresar los datos...")
            continue
        estado = insertar("clientes", temp)
        if(estado):
            input("[EXITO] Presione ENTER para continuar...")
            break
        else:
            input("[ERROR] Presione ENTER para reintentar...")


def editar_cliente():
    while(True):
        clear()
        print("--------------------------------------")
        print("| SUPERMERCADOS SAN PABLO - CLIENTES |")
        print("--------------------------------------")
        print(" ")
        p = input("Ingrese el parametro de busqueda: ")
        v = input("Ingrease el valor del parametro a buscar: ")
        datos = leer("clientes", p, v)
        if(not datos):
            input("[ERROR] Presione ENTER para reingresar los datos...")
            continue
        print("    DATOS DEL CLIENTE:")
        for item in datos:
            keys = list(item.keys())
            valores = list(item.values())
            for i in range(0, len(keys)):
                print("        " + keys[i] + ": " + str(valores[i]))
        nombre = input("Intruduzca nombre del cliente: ")
        if(nombre == "" or not nombre):
            nombre = datos[0]["nombre"]
        ruc = input("Introduzca RUC: ")
        if(ruc == "" or not ruc):
            ruc = datos[0]["ruc"]
        temp = crear_cliente(nombre, ruc)
        if(not temp):
            input("[ERROR] Presione ENTER para reingresar los datos...")
            continue
        estado = editar("clientes", temp, item["id"])
        if(estado == True):
            input("[EXITO] Presione ENTER para continuar...")
            break
        else:
            input("[ERROR] Presione ENTER para continuar...")
            break

def eliminar_cliente():
    while(True):
        clear()
        print("--------------------------------------")
        print("| SUPERMERCADOS SAN PABLO - CLIENTES |")
        print("--------------------------------------")
        print(" ")
        id = int(input("Ingrese el ID del cliente a eliminar: "))
        check = input("Esta seguro de que desea eliminar el cliente? [y/N]: ")
        if(check.upper() == "Y"):
            estado = borrar("clientes", id)
            if(estado):
                input("[EXITO] Presione ENTER para continuar...")
                break
            else:
                input("[ERROR] Presione ENTER para reintentar...")
        else:
            print("El usuario ha cancelado la operacion.")
            input("[EXITO] Presione ENTER para continuar...")
            break


def menu_clientes():
    while(True):
        clear()
        print("--------------------------------------")
        print("| SUPERMERCADOS SAN PABLO - CLIENTES |")
        print("--------------------------------------")
        print(" ")
        print("OPCIONES:")
        print(" ")
        print("    1) CONSULTAR CLIENTES")
        print("    2) REGISTRAR CLIENTE")
        print("    3) ACTUALIZAR DATOS DE CLIENTE")
        print("    4) ELIMINAR CLIENTE")
        print("    0) VOLVER ATRAS")
        print(" ")
        opcion = int(input("Ingrese una opcion valida: "))
        if(opcion == 0):
            break
        if(opcion == 1):
            menu_consultar_clientes()
        if(opcion == 2):
            insertar_clientes()
        if(opcion == 3):
            eliminar_clientes()
        if(opcion == 4):
            break


# Sección de Empleados:
def menu_consultar_empleados():
    while(True):
        clear()
        print("---------------------------------------")
        print("| SUPERMERCADOS SAN PABLO - EMPLEADOS |")
        print("---------------------------------------")
        print(" ")
        print("OPCIONES:")
        print(" ")
        print("    1) MOSTRAR LISTA DE PRODUCTOS")
        print("    2) BUSCAR PRODUCTO")
        print("    0) VOLVER ATRAS")
        print(" ")
        opcion = int(input("Ingrese una opcion valida: "))
        if(opcion == 0):
            break

        if(opcion == 1):
            datos = leer("empleados")
            for item in datos:
                keys = list(item.keys())
                valores = list(item.values())
                print("{")
                for i in range(0, len(keys)):
                    print("    " + keys[i] + ": " + str(valores[i]))
                print("}")
                input("Presione ENTER para ver el siguiente empleado...")
                
        if(opcion == 2):
            p = input("Ingrese el parametro de busqueda: ")
            v = input("Ingrease el valor del parametro a buscar: ")
            datos = leer("empleados", p, v)
            for item in datos:
                keys = list(item.keys())
                valores = list(item.values())
                print("{")
                for i in range(0, len(keys)):
                    print("    " + keys[i] + ": " + str(valores[i]))
                print("}")
                input("Presione ENTER para ver el siguiente empleado...")


def insertar_empleado():
    while(True):
        clear()
        print("---------------------------------------")
        print("| SUPERMERCADOS SAN PABLO - EMPLEADOS |")
        print("---------------------------------------")
        print(" ")
        print("    NUEVO EMPLEADO:")
        print(" ")
        nombre = input("Intruduzca nombre del empleado: ")
        password = input("Introduzca password: ")
        ci = input("Introduzca CI: ")
        cargo = input("Introduzca cargo: ")
        email = input("Introduzca email: ")
        temp = crear_empleado(nombre, password, ci, cargo, email)
        if(not temp):
            input("[ERROR] Presione ENTER para reingresar los datos...")
            continue
        estado = insertar("empleados", temp)
        if(estado):
            input("[EXITO] Presione ENTER para continuar...")
            break
        else:
            input("[ERROR] Presione ENTER para reintentar...")


def editar_empleado():
    while(True):
        clear()
        print("---------------------------------------")
        print("| SUPERMERCADOS SAN PABLO - EMPLEADOS |")
        print("---------------------------------------")
        print(" ")
        p = input("Ingrese el parametro de busqueda: ")
        v = input("Ingrease el valor del parametro a buscar: ")
        datos = leer("empleados", p, v)
        if(not datos):
            input("[ERROR] Presione ENTER para reingresar los datos...")
            continue
        print("    DATOS DEL EMPLEADO:")
        for item in datos:
            keys = list(item.keys())
            valores = list(item.values())
            for i in range(0, len(keys)):
                print("        " + keys[i] + ": " + str(valores[i]))
        nombre = input("Intruduzca nombre del empleado: ")
        if(nombre == "" or not nombre):
            nombre = datos[0]["nombre"]
        # Aquí hay una vulnerrabilidad, pero por ahora la vamos a ignorar, junto al hecho
        # de que nos falta implementar un control de acceso.
        # Lo vamos a ver cuando usemos una Base de Datos y podamos escribir código
        # de manera más fluida.
        password = input("Introduzca password (Por defecto se pone la contrasena \"BLANK\"): ")
        if(password == "" or not password):
            password = "BLANK"
        ci = input("Introduzca CI: ")
        if(ci == "" or not ci):
            ci = datos[0]["ci"]
        cargo = input("Introduzca cargo: ")
        if(cargo == "" or not cargo):
            cargo = datos[0]["cargo"]
        email = input("Introduzca email: ")
        if(email == "" or not email):
            email = datos[0]["email"]
        temp = crear_empleado(nombre, password, ci, cargo, email)
        if(not temp):
            input("[ERROR] Presione ENTER para reingresar los datos...")
            continue
        estado = editar("empleados", temp, item["id"])
        if(estado == True):
            input("[EXITO] Presione ENTER para continuar...")
            break
        else:
            input("[ERROR] Presione ENTER para continuar...")
            break

def eliminar_empleado():
    while(True):
        clear()
        print("---------------------------------------")
        print("| SUPERMERCADOS SAN PABLO - EMPLEADOS |")
        print("---------------------------------------")
        print(" ")
        id = int(input("Ingrese el ID del empleado a eliminar: "))
        check = input("Esta seguro de que desea eliminar el empleado? [y/N]: ")
        if(check.upper() == "Y"):
            estado = borrar("empleados", id)
            if(estado):
                input("[EXITO] Presione ENTER para continuar...")
                break
            else:
                input("[ERROR] Presione ENTER para reintentar...")
        else:
            print("El usuario ha cancelado la operacion.")
            input("[EXITO] Presione ENTER para continuar...")
            break


def menu_empleados():
    while(True):
        clear()
        print("---------------------------------------")
        print("| SUPERMERCADOS SAN PABLO - EMPLEADOS |")
        print("---------------------------------------")
        print(" ")
        print("OPCIONES:")
        print(" ")
        print("    1) CONSULTAR NOMINA")
        print("    2) INSERTAR EMPLEADO")
        print("    3) ACTUALIZAR DATOS DE EMPLEADO")
        print("    4) ELIMINAR EMPLEADO")
        print("    0) VOLVER ATRAS")
        print(" ")
        opcion = int(input("Ingrese una opcion valida: "))
        if(opcion == 0):
            break
        
        if(opcion == 1):
            menu_consultar_empleados()
        
        if(opcion == 2):
            insertar_empleado()
        
        if(opcion == 3):
            editar_empleado()
        
        if(opcion == 4):
            eliminar_empleado()


# Menú principal:
def main_menu():
    while(True):
        clear()
        print("****************************************************")
        print("* SUPERMERCADOS SAN PABLO - SISTEMA ADMINISTRATIVO *")
        print("****************************************************")
        print(" ")
        print("MENU PRINCIPAL:")
        print(" ")
        print("    1) STOCK")
        print("    2) CLIENTES")
        print("    3) EMPLEADOS")
        print("    0) SALIR DEL SISTEMA")
        print(" ")
        opcion = int(input("Ingrese un numero de opcion valido: "))
        
        if(opcion == 1):
            menu_productos()
        
        if(opcion == 2):
            menu_clientes()
        
        if(opcion == 3):
            menu_empleados()
        
        if(opcion == 0):
            break

# Insertamos un usuario Programador del sistema para poder hacer las pruebas.
# En mi caso, simplemente voy a llamarlo "Jakku":
insertar("empleados", crear_empleado("Jakku", "123456", "0000000", "Programador"))

# También insertamos productos de prueba y clientes de prueba para poder probar
# todas las rutinas:
insertar("productos", crear_producto("Lechuga", "Lechuga nacional", 2000, 3000, 50))
insertar("productos", crear_producto("Tomate", "Tomate nacional", 4000, 6000, 50))
insertar("productos", crear_producto("Papa", "Papa negra nacional", 4000, 6000, 50))
insertar("clientes", crear_cliente("Liliana Ortiz", "1234567-8"))

# Ejecutamos el programa principal:
while(not login()):
    continue

main_menu()
pause_exit()
