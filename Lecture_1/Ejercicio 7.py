# Ejercicio 8: ¿Par o impar? ¿Y múltiplo de 5?

numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

if numero % 5 == 0:
    print(f"Y además, {numero} es múltiplo de 5.")
else:
    print(f"Y además, {numero} no es múltiplo de 5.")
