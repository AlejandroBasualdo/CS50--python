# Hacer una calculadora donde el usuario ingrese: 1- el total de la cuenta, 2- el porcentaje de propina que desea dejar
# El programa debe mostrar cuanto fue de cuenta, el total final de la propina

def total_cuenta():
    total = float(input("Ingrese el total de la cuenta: "))
    return total
    
def porcentaje_propina():
    porcentaje = float(input("Ingrese el porcentaje de propina que desea dejar: "))
    return porcentaje

def calcular_propina():
    total: float = total_cuenta()
    porcentaje: float = porcentaje_propina()
    propina= (total * porcentaje) / 100
    total_final = total + propina
    return total, porcentaje, propina, total_final

total, porcentaje, propina, total_final = calcular_propina()

print(f"El total de la cuenta es: ${total:.2f}")
print(f"El porcentaje de la propina fue:{porcentaje:.2f}%")
print(f"Propina:${propina:.2f}")
print(f"Total con propina fue de:${total_final:.2f}")


