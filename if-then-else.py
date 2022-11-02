# Ahora que ya sabemos como leer e introducir datos desde el teclado y podemos mostrar una salida al usuario,
# vamos a ver como tomar decisiones basadas en dichas entradas o incluso variables.
check = int(input("Ingrese un entero negativo: "))
if (check >= 0):
    print("ERROR")
    exit(1)
print("Se ha comprobado que el usuario es un humano.")

# Podemos crear una condición alternativa con la palabra clave else.
# De este modo, si se cumple la condición se ejecuta lo que sigue al if.
# En caso contrario, se ejecuta lo que siga al else.
# Ejemplo:
a = int(input("Ingresa un entero: "))
b = int(input("Ingresa otro entero: "))
if (a > b):
    print(str(a) + " es mayor que " + str(b))
else:
    print("O bien " + str(b) + " es mayor que " + str(a) + ", o " + str(a) + " y " + str(b) + " son iguales.")
input("Presione ENTER para continuar...")
exit(0)
