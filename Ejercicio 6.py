# Detector de número par o impar

def par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero =int(input("Ingresa un numero: "))
if par(numero):
    print(f"El numero {numero} es par.")
else:
    print(f"El numero {numero} es impar.")
