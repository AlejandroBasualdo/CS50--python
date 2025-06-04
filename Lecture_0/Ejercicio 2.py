# Escribe un programa que le pida al usuario una cantidad de minutos y convierta ese tiempo a: dias, horas y minutos restantes.

def convertir_tiempo(minutos):
    dias = minutos // 1440
    horas = (minutos % 1440) // 60
    minutos_restantes= minutos % 60

    return dias, horas, minutos_restantes

minutos = int(input("Ingrese la cantidad de minutos: "))
dias, horas, minutos_restantes = convertir_tiempo(minutos)

print(f"{minutos} minutos son {dias} días, {horas} horas y {minutos_restantes} minutos restantes.")
