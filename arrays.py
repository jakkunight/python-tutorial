# Veamos qué son los arrays.
# Un array, o lista, es una ESTRUCTURA DE DATOS que organiza sus elementos de manera ordenada, de modo que cada elemento
# está indexado según su posición en la misma.
# Veamos un ejemplo:
lista = [
    "J",
    "a",
    "k",
    "k",
    "u"
]

# Podemos referirnos a cada elemento mediante su posición en la misma de la siguiente forma:
# nombre_lista[número_elemento]
print(lista[0]) # Corresponde al primer elemento de la lista.

# Es evidente que, si necesitamos tratar todos los elementos de la misma manera, el bucle for es nuestro mejor aliado:
for i in range(0, len(lista)):
    print(lista[i], end="") # El "end=""" indica que el carácter de "fin de línea" es un carácter "nulo" (ASCII = 0)
print(" ")

# También podemos hacer cosas más interesantes con el for y las listas:
for elemento in lista:
    print(elemento, end="")
print(" ")

# Podemos hacer búsqudas de elementos dentro de la misma mediante un if:
if ("J" in lista):
    print("Encontramos una 'J'!")

# Podemos añadir elementos al final de la lista usando el método append():
lista.append(" ")
lista.append("N")
lista.append("i")
lista.append("g")
lista.append("h")
lista.append("t")

for elemento in lista:
    print(elemento, end="")
print(" ")

# Por supuesto, también podemos ocupar la operación contraria con el método pop():
lista.pop()
lista.pop()
lista.pop()
lista.pop()
lista.pop()
lista.pop()

for elemento in lista:
    print(elemento, end="")
print(" ")

# Otros métodos útiles son:
# * sort(): Ordena la los elementos de la lista.
# * extend(valor): Igual que append(), pero también permite añadir otros arrays.
# * count(valor): Devuelve la cantidad de elementos que tengan valor igual a "valor".
# * pop(índice): Remueve el elemento especificado en la posición "índice".
# * clear(): Remueve todos los elementos dentro del array.
# * insert(índice): Inserta un nuevo elemento vacío en la posición "índice".
# * copy(): Devuelve una copia de la lista.
# * reverse(): Retorna una la lista en orden inverso. 

# Terminamos la ejecución:
input("Presione ENTER para continuar...")
exit(0)
