# Veamos el bucle for.
# Este bucle, no se define como normalmente acostumbran el resto de lenguajes, sino que se define de manera muy particular.
# Veamos un ejemplo de ello.
print("TABLA del 5:")
for i in range(0, 11): # range() le da valor inicial al índice y define un valor límite para el for.
    print("5 * " + str(i) + " = " + str(5 * i))
# Terminamos el programa:
input("Presione ENTER para continuar...")
exit(0)
