# Vamos a ver como hacer un bucle del tipo REPEAT-UNTIL en Python.
# Lo primero a saber, es que no hay una única manera de hacerlo.
# Lo segundo a saber, es que Python no trae de foma nativa este bucle.
# Veamos una de las formas, la más simple, para hacerlo.
# Escribimos una vez el bloque de instrucciones a ejecutar dentro del bucle, fuera del mismo:
usuario = input("Ingrese su nombre de usuario: ")
password = input("Ingrese su contrasena: ")
# Luego lo metemos dentro de un while:
while (not usuario == "Jakku" or  not password == "123456"): # Aquí el not niega la condición y el or implica que
    usuario = input("Ingrese su nombre de usuario: ")        # mientras una de las condiciones sea verdadera
    password = input("Ingrese su contrasena: ")              # toda la condición lo es.
print("Bienvenido/a " + usuario + "!")                       # Si quisiéramos que ambas sean verdad, usamos el operador
                                                             # and, en lugar del or.
# Podemos tambien utilizar esta otra manera:
while True: # Indica que el bucle se ejecuta "infiniitas" veces.
    usuario = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contrasena: ")
    if (usuario == "Jakku" and password == "123456"):
        break # break termina el bucle de manera abrupta.
print("Bienvenido/a " + usuario + "!")
input("Presione ENTER para continuar...")
exit(0)
