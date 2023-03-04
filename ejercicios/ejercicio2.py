#!/usr/bin/python
# Crear un programa que lea una tabla con los nombres, edad, sexo y notas de algoritmia de
# un curso de alumnos de un colegio. El programa debe calcular e imprimir en base a estos datos
# estadísticas fundamentales (promedio, moda, porcentajes, etc).
# Desafío secreto:
# Descubre como mejorar el programa considerando más cosas que tus compañeros.
# Puedes añadir sistemas que, en base a lo calculado, impriman una conclusión lógica al
# usuario

# Creamos una clase para modelar un "Alumno":
class Alumno:
    # Definimos un constructor para la clase:
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.sexo = None
        self.nota_algoritmia = None

# Carga de datos:
# Nombres:
def ingresar_nombre():
    return input("Ingrese su nombre: ")

# Edades:
def ingresar_edad():
    aux = int(input("Ingrese su edad: "))
    while(aux <= 0):
        aux = int(input("Ingrese su edad: "))
    return aux

# Sexo:
def ingresar_sexo():
    aux = input("Ingrese su sexo [f/M]: ")
    if(aux.upper() != "F"):
        aux = "M"
    return aux.upper()

# Notas:
def ingresar_notas():
    aux = int(input("Ingrese su nota de algoritmia: [1-5]: "))
    while(aux < 1 or aux > 5):
        aux = int(input("Ingrese su nota de algoritmia: [1-5]: "))
    return aux

# Montamos la tabla de datos:
# Creamos una variable para armar la tabla de datos:
print("======== Entrada de datos ========")
temp = Alumno()
temp.nombre = ingresar_nombre()
temp.edad = ingresar_edad()
temp.sexo = ingresar_sexo()
temp.nota_algoritmia = ingresar_notas()
Tabla = [temp]
eod = False
while(not eod):
    print("==============================")
    temp = Alumno()
    temp.nombre = ingresar_nombre()
    temp.edad = ingresar_edad()
    temp.sexo = ingresar_sexo()
    temp.nota_algoritmia = ingresar_notas()
    Tabla.append(temp)
    aux = input("Quieres agregar otro elemento [Y/n]? ")
    if(aux.upper() == "N"):
        eod = True

# Procesamos los datos:
promedio_notas = 0
promedio_edad = 0
moda_edad = 0
moda_notas = 0
porcentaje_notas = [0, 0, 0, 0, 0]

for i in range(0, len(Tabla)):
    promedio_notas += Tabla[i].nota_algoritmia
    promedio_edad += Tabla[i].edad
    for j in range(0, 5):
        if(Tabla[i].nota_algoritmia == j):
            porcentaje_notas[j - 1] += 1
#moda_notas = 
    

# Imprimimos los resultados:
print("Promedio de Notas del curso: ", promedio_notas / len(Tabla))
print("Promedio de Edad del curso: ", promedio_edad / len(Tabla))




