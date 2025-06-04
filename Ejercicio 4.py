# Conversor de temperatura (°C a °F)

def temp(celcius):
    farenheit = (celcius * 9/5) + 32
    return farenheit

celcius = float(input("Ingresa la temperatura en grados celcius(°C): "))

temp_convertida = temp(celcius)

print(f"La temperatura dada en grados celcius(°C) fue de: {celcius:.2f}°C")
print(f"La temperatura convertida de celcius a farenheit(°F) es: {temp_convertida:.2f}°F")
