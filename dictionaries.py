# Veamos que son los diccionarios.
# Un diccionario es una ESTRUCTURA DE DATOS que, similar a un array, permite almacenar una colección
# de elementos que se definen como pares "clave-valor" o "key-value" (De ahí que se los llame diccionarios).
# Veamos un ejemplo:
diccionario = {
    "C": "\"Nada es mejor que C\" (Linus Torvalds, creador de Linux)",
    "C++": "El mejor lenguaje de programación.",
    "Java": "El lenguaje de programación más odiado por a comunidad.",
    "Kotlin": "Lo mismo que Java, pero todos lo aman.",
    "Python": "El lenguaje de programación para noobs.",
    "JavaScript": "El lenguaje de programación que es \"Rey de la Web\"",
    "TypeScript": "JavaScript, pero con esteroides.",
    "Rust": "C++ recargado.",
    "Swift": "El lenguaje de programación para los fans de Steve Jobs y Apple.",
    "Assembly": "El lenguaje de programación para los frikis de la informática."
}

# Entonces podemos hacer algo como esto:
lenguaje = input("Consulta sobre un lenguaje de programación: ")
print(lenguaje + ": " + diccionario[lenguaje])

# Lo mejor de los diccionarios, es que permiten improvisar un "switch-case" en algunos casos:
print(diccionario[input("Mira lo que opino de un lenguaje de programación: ")])

# Aquí el diccionario hizo del bloque:
# match clave
#     case clave1:
#         variable = valor1
#         print(variable)
#     case clave2:
#         variable = valor2
#         print(variable)
# ...

# Como vemos, los diccionarios son estructuras muy útiles y convenientes.

# Finalizamos el programa:
input("Presione ENTER para continuar...")
exit(0)
