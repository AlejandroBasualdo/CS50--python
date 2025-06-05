#Ejercicio 2: “Clasificador de Edad”
#Objetivo: Practicar el uso de input(), conversión de tipos (de texto a número), y estructuras condicionales (if, elif, else).


edad = input("¿Cuál es tu edad? ").strip()

#nueva funcion descubierta
# isdigit crea el valor a poitivo solamente, es decir que los negativos o decimales no los acepta

if edad.isdigit():
    edad = int(edad)

    if edad < 0:
        print("Edad no válida. No puedes tener una edad negativa.")
    elif edad >= 12:
        print("Eres un niño.")
    elif edad < 13 and edad <= 17:
        print("Eres un adolescente.")
    elif edad < 18 and edad <= 64:
        print("Eres un adulto.")
    else:
        print("Eres un adulto mayor.")
else:
    print("Por favor, ingresa un número válido para la edad.")