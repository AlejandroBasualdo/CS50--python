# Conversor de tiempo total en segundos a días, horas, minutos y segundos

def convertir_tiempo(segundos):
    dias: int = segundos // 86400
    horas: int = (segundos % 86400) // 3600
    minutos: int =(segundos % 3600) // 60
    segundos_restantes: int = segundos % 60
    return dias, horas, minutos, segundos_restantes

segundos = int(input("Ingrese la cantidad de segundos: "))
dias, horas, minutos, segundos_restantes = convertir_tiempo(segundos)

print(f"{segundos} segundos son {dias} días, {horas} horas, {minutos} minutos y {segundos_restantes} segundos restantes.")
