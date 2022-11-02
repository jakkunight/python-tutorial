# Ejemplo de instrucción para pedir datos al usuario por teclado (prompt):
nombre = input("Ingrese su nombre de usuario: ")

# El dato devuelto pot la función built-in input() SIEMPRE es un STRING (cadena de caracteres o texto).
# Si la entrada que preciamos es de otro tipo, por ejemplo un número, debemos usar el constructor de la clase
# correspondiente para hacerlo.
# Ejemplo:
a = int(input("Ingrese un numero entero: "))
b = int(input("Ingrese otro numero entero: "))

# Si quisiéramos que el número sea un número real, entonces debemos usar float() en lugar de int()
# Ejemplo:
f1 = float(input("Ingrese un numero real: "))
f2 = float(input("Ingrese otro numero real: "))

# Supongamos que queremos mostrar un mensaje por pantalla para finalizar.
# En este caso, vamos a mostrar el nombre del usuario y la suma de los enteros y los reales.
print("El usuario " + nombre + " ha ingresado los enteros " + str(a) + " y " + str(b) + ", y los reales " + str(f1) + " y " + str(f2))
print("La suma de los enteros es: " + str(a + b))
print("La suma de los reales es: " + str(f1 + f2))
input("Presione ENTER para continuar...") # Lo ponemos para evitar el cierre del programa y visualizar el resultado.
# Terminamos el programa explícitamente y retornamos un código de error con exit().
# Por convención, el cero indica que el programa ha terminado sin errores.
exit(0)
