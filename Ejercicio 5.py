# Calculadora de propina avanzada

def total_cuenta():
    total = float(input("Ingresa el total de la cuenta: "))

    return total

def porcentaje_propina():
    porcentaje = float(input("Que porcentaje de propina desea dejar? "))

    return porcentaje

def div_personas():
    personas = int(input("Cuantas personas van a pagar la cuenta? "))
  
    

    return personas

def calcular_propina():
    total = total_cuenta()
    porcentaje = porcentaje_propina()
    personas = div_personas()
    propina = (total * porcentaje) / 100
    total_persona = (total + propina) / personas
    total_final = total + propina
    return total, porcentaje, personas, propina, total_persona, total_final

total, porcentaje, personas, propina, total_persona, total_final = calcular_propina()

print(f"Total de la cuenta: ${total:.2f}")
print(f"Porcentaje de propina: {porcentaje:.2f}%")
print(f"Propina: ${propina:.2f}")
print(f"Total con propina: ${total_final:.2f}")


if personas == 1:
    print("Total a pagar por la persona: $", total_persona)
else:
    print(f"Total a pagar por cada persona: ${total_persona:.2f}")
