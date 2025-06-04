# Calculadora de área y perímetro de un rectángulo

def cal_area():
    print("AREA")
    base = float(input("Ingresa el valor de la base del rectángulo para el: "))
    altura = float(input("Ingresa el valor de la altura del rectángulo: "))
    return base * altura

area = cal_area()

def cal_perimetro():
    print("PERÍMETRO")
    base = float(input("Ingresa el valor de la base del rectángulo: "))
    altura = float(input("Ingresa el valor de la altura del rectángulo: "))
    return 2 * (base + altura)

perimetro = cal_perimetro()

print(f"El área del rectángulo es: {area:.2f}")
print(f"El perímetro del rectángulo es: {perimetro:.2f}")