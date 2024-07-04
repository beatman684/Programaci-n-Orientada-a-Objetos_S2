# Definición de la clase base 'Animal'
class Animal:
    def __init__(self, nombre):
        self.__nombre = nombre  # Encapsulación del atributo nombre

    def get_nombre(self):
        return self.__nombre

    def sonido(self):
        pass  # Método a ser sobrescrito en las clases derivadas


# Definición de la clase derivada 'Perro' que hereda de 'Animal'
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.__raza = raza  # Encapsulación del atributo raza

    def get_raza(self):
        return self.__raza

    def sonido(self):
        return "¡Guau! ¡Guau!"


# Definición de la clase derivada 'Gato' que hereda de 'Animal'
class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.__color = color  # Encapsulación del atributo color

    def get_color(self):
        return self.__color

    def sonido(self):
        return "¡Miau! ¡Miau!"


# Función principal del programa
def main():
    # Creación de instancias de las clases
    perro1 = Perro("Firulais", "Labrador")
    gato1 = Gato("Garfield", "Naranja y blanco")

    # Accediendo a métodos y atributos de las instancias
    print(f"{perro1.get_nombre()} es un perro de raza {perro1.get_raza()}. Dice: {perro1.sonido()}")
    print(f"{gato1.get_nombre()} es un gato de color {gato1.get_color()}. Dice: {gato1.sonido()}")


# Ejecución del programa
if __name__ == "__main__":
    main()
