#!/usr/bin/python
# Ahorcado!
# Programa un juego de ahorcado en Python para dos jugadores.
# El Jugador 1 ingresa una palabra para que el Jugador 2 la adivine.
# El Jugador 2 posee seis intentos para adivinar la palabra.
# El programa debe permitir volver a jugar y llevar registro de las victorias y derrotas
# de cada jugaador. También debe permitir nombrar a los jugadores.

# Definimos algunas clases útiles:
class Jugador:
    def __init__(self):
        self.nombre = ""
        self.puntuacion = 0
    def nombrar(self, nombre):
        self.nombre = nombre
    def incrementar_puntos(self):
        self.puntuacion += 1

class Jugador1(Jugador):
    def __init__(self):
        super().__init__()
        self.palabra = ""
    def cargar_palabra(self, palabra):
        self.palabra = palabra

class Jugador2(Jugador):
    def __init__(self):
        super().__init__()
        self.vidas = 6
        self.aciertos = []
    def reducir_vidas(self):
        self.vidas -= 1
    def cargar_aciertos(self, palabra):
        for letra in palabra:
            if(letra == " "):
                self.aciertos.append(letra)
                continue
            self.aciertos.append("_")
    def incrementar_aciertos(self):
        pass


# Definimos una rutina para limpiar la pantalla y posicionar el cursor en el inicio de
# la pantalla:
def clear():
    print("\033[2J")
    print("\033[0;0f")

# Lógica del juego:
clear()
J1 = Jugador1()
J2 = Jugador2()
J1.nombrar(input("Ingrese nombre del jugador 1: "))
J2.nombrar(input("Ingrese nombre del jugador 2: "))
while(True):
    clear()
    from getpass import getpass
    J1.cargar_palabra(getpass("Ingresa una palabra para que " + J2.nombre + " la adivine: "))
    J2.cargar_aciertos(J1.palabra)
    while(True):
        clear()
        print("=============")
        print("| AHORCADO! |")
        print("=============")
        print("Vidas: " + str(J2.vidas))
        for char in J2.aciertos:
            print(char, end="")
        print(" ")
        letra = input("Ingresa una letra: ")
        check = False
        for i in range(0, len(J1.palabra)):
            if(letra.upper() == J1.palabra[i].upper()):
                check = True
                J2.aciertos[i] = J1.palabra[i]
        if(not check):
            J2.reducir_vidas()
        if(not "_" in J2.aciertos):
            clear()
            print(J2.nombre + " ha ganado!!!")
            J2.incrementar_puntos()
            break
        if(J2.vidas == 0):
            clear()
            print(J1.nombre + " ha ganado!!!")
            J1.incrementar_puntos()
            break
    opt = input("Quieren jugar de nuevo? [Y/n]: ")
    if(opt.upper() == "N"):
        print("Total de puntos:")
        print(J1.nombre + ": " + str(J1.puntuacion))
        print(J2.nombre + ": " + str(J2.puntuacion))
        print("Hasta la proxima!")
        break
    
