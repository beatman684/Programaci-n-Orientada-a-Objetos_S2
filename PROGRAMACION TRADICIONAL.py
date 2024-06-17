# Implementación utilizando estructuras de funciones

def ingresar_temperaturas_diarias():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

def main():
    temperaturas = ingresar_temperaturas_diarias()
    promedio = calcular_promedio_semanal(temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}")

if __name__ == "__main__":
    main()
