# Escribe un programa que:Pregunte al usuario su peso en kilogramos, Pregunte su estatura en metros, Calcule el IMC usando la fórmula:

def IMC(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu estatura en metros: "))

IMC_total = IMC(peso, altura)

print(f"Tu IMC es: {IMC_total:.2f}")