#Me saludas, por favor

nombre = input("¿Cuál es tu nombre? ").strip()

if not nombre:
    print("No has ingresa tu nombre.")
elif "profesor" in nombre.lower():
    print("¡Hola profesor!")
else:
    print(f"¡Hola {nombre}!")