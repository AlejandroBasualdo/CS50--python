# Calculadora de IMC (Índice de Masa Corporal)

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("¿Cuál es tu peso en kg? ").strip())

altura = float(input("¿Cuál es tu altura en metros? ").strip())

IMC = calcular_imc(peso, altura)

if IMC < 18.5:
    print(f"Tu IMC es {IMC:.2f}. Estás por debajo del peso normal.")
elif IMC <= 24.9:
    print(f"Tu IMC es {IMC:.2f}. Tienes un peso normal.")
elif IMC <= 29.9:
    print(f"Tu IMC es {IMC:.2f}. Tienes sobrepeso.")   
else:
    print(f"Tu IMC es {IMC:.2f}. Tienes obesidad.")