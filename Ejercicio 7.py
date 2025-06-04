# Calculadora de edad

def cal_edad():
    año_nacimiento = int(input("En que año naciste? "))
    fecha_actual = int(input("En que año estamos? "))
    edad = fecha_actual - año_nacimiento
    return edad
edad = cal_edad() 

futuro = edad + 5 

print(f"Tu edad es: {edad} años.")
print(f"En 5 años tendras: {futuro} años.")
