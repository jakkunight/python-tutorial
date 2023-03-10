#!/usr/bin/python
# Triángulos!
# En todo triángulo de lados a, b y c, se cumple que la longitus de todos los lados es menor
# que la suma de las longitudes de los otros dos lados.
# Escriba un programa que verifique si tres números son o no las longitudes de los lados de
# un triángulo.
# El programa debe permitir hacer de nuevo el cálculo sin necesidad de volver a ejecutarlo.

while(True):
    a = 0.0
    b = 0.0
    c = 0.0
    while(True):
        try:
            a = float(input("Ingrese una longitud valida para el lado a: "))
            if(a > 0.0):
                break
        except:
            continue
    while(True):
        try:
            b = float(input("Ingrese una longitud valida para el lado b: "))
            if(b > 0.0):
                break
        except:
            continue
    while(True):
        try:
            c = float(input("Ingrese una longitud valida para el lado c: "))
            if(c > 0.0):
                break
        except:
            continue
    if(a >= b + c or b >= a + c or c >= a + b):
        print("Los lados no corresponden con un triangulo!!!")
    else:
        print("Los lados corresponden con un triangulo!!!")
    if(input("Quieres probar otra vez? [Y/n]").upper() == "N"):
        break

print("Hasta la proxima!")
