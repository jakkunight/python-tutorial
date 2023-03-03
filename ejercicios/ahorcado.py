#!/usr/bin/python
# Ahorcado!
# Programa un juego de ahorcado en Python.

# Creamos un diccionario con las palabras que vamos a usar para el juego:
diccionario = [
    "Paraguay",
    "Argentina",
    "Brasil",
    "Uruguay",
    "Chile",
    "Ecuador",
    "Bolivia",
    "Venezuela",
    "Colombia",
    "Peru",
    "Surinam",
    "Guyana Francesa",
    "Guayana Holandesa"
]

# Definimos algunas variables globales de nuestro juego:
vidas_totales = 6
vidas = 6
palabra = ""
fin = False
log = []

# Importamos lo necesario para trabajar:
import random

# Creamos una bonita pantalla de bienvenda:
def bienvenida():
    print("======================================")
    print("| Bienvenido al juego de AHORCADO!!! |")
    print("======================================")
    print("**** Reglas ****")
    print(" 1) El programa elige una palabra al azar de su diccionario de palabras.")
    print(''' 2) El usuario debe tratar de adivinar la palabra elegida. El jugador debe ingresar una letra. Si la misma está contenida
    en la palabra, se mostraran en su posicion correspondiente todas las letras que coincidan con la misma. En caso contrario, 
    se le restaran vidas de las SEIS (6) que posee el jugador hasta que se complete la figura del "ahorcado", lo cual indica que el 
    jugador ha perdido el juego, revelandose la palabra elegida.''')

# Creamos la rutina que muestra el cuerpo del "ahorcado":
def mostrar_ahorcado(vidas_actuales):
    global vidas_totales
    horca = [
        " +=====+",
        " |     |",
        " |   ",
        " |   ",
        " |   ",
        " |   ",
        " |   ",
        " |   ",
        "================",
        "|** AHORCADO **|",
        "================"
    ]
    ahorcado = [
        " www",
        "(x,x)",
        " /|\\",
        "  |",
        " / \\",
        "/   \\",
    ]
    for i in range(0, 11):
        if(i < 2 or i > 7):
            print(horca[i])
        else:
            if(i - 2 < vidas_totales - vidas_actuales):
                print(horca[i] + ahorcado[i - 2])
            else:
                print(horca[i])

# Creamos una función para elegir la palabra y cargarla en la variable global:
def setup():
    global palabra
    global log
    palabra = diccionario[random.randint(0, 12)]
    log = ["_"] * len(palabra)
    

# Creamos una rutina para mostrar los aciertos al jugador:
def console():
    print(" ")
    global palabra, log, vidas
    for letter in log:
        print(letter, end=" ")
    print("Vidas: " + str(vidas))
    letra = input("Ingrese una letra: ")
    ahorcar = True
    for i in range(0, len(palabra)):
        if(palabra[i].upper() == letra.upper()):
            log[i] = letra.upper()
            ahorcar = False
    if(ahorcar == True):
        vidas -= 1
    win = True
    for ch in log:
        if(ch == "_"):
            win = False
    if(win == True):
        print("GANASTE!!!")
        finalizar_juego()
    if(vidas == 0):
        print("PERDISTE!!!")
        finalizar_juego()

# Creamos la rutina para finalizar el juego:
def finalizar_juego():
    global fin
    respuesta = input("Quieres volver a jugar? [Y/n]")
    while(respuesta != "y" and respuesta != "n" and respuesta != "Y" and respuesta != "N"):
        print(respuesta)
        respuesta = input("Quieres volver a jugar? [Y/n]")
    if(respuesta == "Y" or respuesta == "y"):
        fin = False
    if(respuesta == "N" or respuesta == "n"):
        fin = True


# Juego:
while (True):
    bienvenida()
    setup()
    while(fin != True):
        console()
