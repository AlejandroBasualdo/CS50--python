# Ejercicio 9: Calculadora de descuentos

precio = float(input("Ingresa el precio del producto: "))

if precio < 50:
    descuento = 0

elif precio >= 50 and precio <= 100:
    descuento = 10

elif precio >= 101 and precio <= 200:
    descuento = 15
else:
    descuento = 20

monto_descuento = precio * descuento / 100
precio_final = precio - monto_descuento

print(f"Monto del producto: ${precio:.2f}")
print(f"Se aplicó un descuento del {descuento}% (${monto_descuento:.2f})")
print(f"Total a pagar: ${precio_final:.2f}")