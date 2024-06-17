# Implementación utilizando el paradigma de POO

class RegistroClima:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas_diarias(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio_semanal(self):
        if len(self.temperaturas) == 0:
            return 0
        promedio = sum(self.temperaturas) / len(self.temperaturas)
        return promedio

def main():
    registro = RegistroClima()
    registro.ingresar_temperaturas_diarias()
    promedio = registro.calcular_promedio_semanal()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}")

if __name__ == "__main__":
    main()
