#Clasificación de temperatura

temp = float(input("¿Cuál es la temperatura en grados Celsius? ").strip())

if temp <= 0:
    print("Esta congelado")
elif temp < 18:
    print("Hace frio")
elif 19 <= temp <= 30:
    print("clima agradable")
else :
    print("Hace mucho calor")