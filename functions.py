# Ahora vamos a ver como hacer para "dividir y conquistar".
# Para ello vamos a crear algo llamado función.
# Una función es un bloque de código que puede ser reutilizado. Puede recibir parámetros y retornar una salida.
# Ejemplo:
def suma (a, b):
    return a + b # La palabra clave return indica que la función debe devolver el valor que se especifique.
def resta (a, b):
    return a - b
def multiplicacion (a, b):
    return a * b
def division (a, b):
    return a / b
def factorial (n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
def potenciacion (a, b):
    return a ** b
def menu ():
    print("LISTA de OPERACIONES:")
    print("1) SUMA")
    print("2) RESTA")
    print("3) MULTIPLICACION")
    print("4) DIVISION")
    print("5) FACTORIAL")
    print("6) POTENCIACION")
    return # Si no se especifica nada, return acaba con la función.

end = False
while (end == False):
    menu()
    op = int(input("Ingrese la operacion a realizar: "))
    if (op == 1):
        a = int(input("Ingrese in numero entero: "))
        b = int(input("Ingrese otro numero entero: "))
        print(str(suma(a, b)))
    if (op == 2):
        a = int(input("Ingrese in numero entero: "))
        b = int(input("Ingrese otro numero entero: "))
        print(str(resta(a, b)))
    if (op == 3):
        a = int(input("Ingrese in numero entero: "))
        b = int(input("Ingrese otro numero entero: "))
        print(str(multiplicacion(a, b)))
    if (op == 4):
        a = int(input("Ingrese in numero entero: "))
        b = int(input("Ingrese otro numero entero: "))
        print(str(division(a, b)))
    if (op == 5):
        a = int(input("Ingrese in numero entero: "))
        print(str(factorial(a)))
    if (op == 6):
        a = int(input("Ingrese in numero entero: "))
        b = int(input("Ingrese otro numero entero: "))
        print(str(potenciacion(a, b)))
    if (op != 1 and op != 2 and op != 3 and op != 4 and op != 5 and op != 6):
        continue
    print("Quieres hacer otra operacion? [Y/n]")
    cont = input()
    if (cont == "N" or cont == "n"):
        end = True
input("Presione ENTER para continuar...")
exit(0)
