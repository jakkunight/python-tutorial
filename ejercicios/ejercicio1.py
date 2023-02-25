#!/usr/bin/python
# Ejercicio 1:
# Crear un programa que lea la base y la altura de un triángulo rectángulo y calcule
# su PERÍMETRO y su ÁREA e imprima ambos resultados.
# Desafío secreto:
# Descubre como mejorar el programa considerando más detalles que tus compañeros.

# Importamos la librería 'math' para hacer operaciones matemáticas complejas:
import math

# Leemos los datos necesarios:
base = float(input("Ingrese una longitud valida para la base: "))
while(base <= 0):
    print("Longitud invalida.")
    base = float(input("Ingrese una longitud valida para la base: "))
es_hipotenusa = int(input("Es la base la HIPOTENUSA? [0/1]: "))
while(es_hipotenusa < 0 and es_hipotenusa > 1):
    print("Respuesta no valida. Ingrese de nuevo el dato. [0/1]")
    es_hipotenusa = int(input("Es la base la HIPOTENUSA? [0/1]: "))
altura = float(input("Ingrese una longitud valida para la atura: "))
while(altura <= 0 or (altura >= base and es_hipotenusa == 0)):
    print("Longitud invalida.")
    altura = float(input("Ingrese una longitud valida para la altura: "))

# Declaramos la hipotenusa y los lados del triángulo:
hipotenusa = 0.0
a = 0.0
b = 0.0
perimetro = 0.0

# Hallamos el área:
area = base * altura / 2

# Definimos ante qué caso estamos:
if(es_hipotenusa == 0):
    # La base es la hipotenusa:
    x = (math.sqrt(base * base - 4 * altura * altura) - base) / 2
    y = (- math.sqrt(base * base - 4 * altura * altura) - base) / 2
    a = math.sqrt(altura * altura + x * x)
    b = math.sqrt(altura * altura + y * y)
    perimetro = a + b + base
else:
    # La base es un cateto:
    hipotenusa = math.sqrt(base * base + altura * altura)
    perimetro = hipotenusa + base + altura

# Imprimimos los resultados:
print("Area del triangulo: " + str(area))
print("Perimetro del triangulo: " + str(perimetro))
