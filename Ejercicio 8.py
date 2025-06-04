# Clasificador de calificaciones

def calif(promedio):
    if 90 <=  promedio <= 100:
        return "Excelente"
    elif promedio >= 80 and promedio <= 89:
        return "Notable"
    elif promedio >= 70 and promedio <= 79:
        return "Aprobado"
    elif promedio >= 0 and promedio <=69:
        return "Reprobado"
    else:
        return "Calificacion no valida"
    
promedio= float(input("Ingresa tu promedio: "))
resultado = calif(promedio)
print(f"Tu promedio final es: {promedio:.2f}")
print(f"Tu calificacion es: {resultado}")