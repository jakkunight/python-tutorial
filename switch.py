# Ahora vamos a ver la estructura SWITCH-CASE en Python.
# Ya que, al igual que el REPEAT-UNTIL, Python no trae por defecto la estructura, la tendremos que crear.
# Vamos a concatenar varios if's, para poder hacerlo más versátil.
sw = int(input("Ingrese un entero: "))
if (sw == 0):
    print(str(sw + 8))
if (sw == 1):
    print(str(sw - 2))
if (sw == 2):
    print(str(sw ** 2)) # El operador ** hace sw elevado a 2.
if (sw == 3):
    print(str(sw / 5)) # El operador / hace la división real entre sw y 5.
if (sw != 0 and sw != 1 and sw != 2 and sw != 3):
    print("ERROR")

# Si usamos la versión 3.10 de Python, entonces podemos utilizar la estructura sin más.
# Ejemplo:
argument = int(input("Ingrese un numero entero: "))
match argument:
    case 0:
        print("zero")
    case 1:
        print("one")
    case 2:
        print("two")
    case default:
        print("number")
input("Presione ENTER para continuar...")
exit(0)
