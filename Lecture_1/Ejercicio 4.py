#Ejercicio 4: Palíndromo

def pali(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    return palabra == palabra[::-1]

input_usuario = input("Introduce una palabra o frase: ")
if pali(input_usuario):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
    