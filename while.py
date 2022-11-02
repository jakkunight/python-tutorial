# Ahora que ya sabemos como evaluar condiciones, vamos a profundizar en los bucles.
# En Python, el único bucle que existe como tal es el while.
# Ejemplo:
alumnos_totales = int(input("Ingrese el numero de alumnos en el curso: "))
alumno = 0
suma_notas = 0
promedio = 0
while (alumno < alumnos_totales):
    nota = int(input("Ingrese la nota en algoritmia del alumno " + str(alumno + 1) + ": "))
    if (nota < 1 or nota > 5):
        print("ERROR")
        continue # Salta a la siguiente iteración del bucle.
    suma_notas += nota
    alumno += 1
promedio = suma_notas // alumnos_totales # Realiza la división entera entre suma_notas y alumnos_totales.
print("El promedio de las notas en algoritmia de este curso es: " + str(promedio))
input("Presione ENTER para continuar...")
exit(0)
