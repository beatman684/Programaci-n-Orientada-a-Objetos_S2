# Función para añadir un nuevo estudiante al registro
def agregar_estudiante(estudiantes, nombre, edad, calificacion):
    """
    Agrega un nuevo estudiante al registro.

    Parámetros:
    estudiantes (list): La lista de estudiantes.
    nombre (str): El nombre del estudiante.
    edad (int): La edad del estudiante.
    calificacion (float): La calificación del estudiante.
    """
    estudiante = {
        'nombre': nombre,
        'edad': edad,
        'calificacion': calificacion
    }
    estudiantes.append(estudiante)

# Función para mostrar todos los estudiantes registrados
def mostrar_estudiantes(estudiantes):
    """
    Muestra todos los estudiantes registrados.

    Parámetros:
    estudiantes (list): La lista de estudiantes.
    """
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Calificación: {estudiante['calificacion']}")

# Función principal para gestionar el registro de estudiantes
def main():
    """
    Función principal que gestiona el registro de estudiantes.
    Permite agregar estudiantes y mostrar la lista de estudiantes.
    """
    estudiantes = []
    while True:
        print("\nRegistro de Estudiantes")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Ingresa el nombre del estudiante: ")
            edad = input("Ingresa la edad del estudiante: ")
            calificacion = input("Ingresa la calificación del estudiante: ")

            # Validar que edad y calificación sean números
            if edad.isdigit() and calificacion.replace('.', '', 1).isdigit():
                edad = int(edad)
                calificacion = float(calificacion)
                agregar_estudiante(estudiantes, nombre, edad, calificacion)
                print("Estudiante agregado exitosamente.")
            else:
                print("Edad y calificación deben ser números válidos.")

        elif opcion == '2':
            mostrar_estudiantes(estudiantes)

        elif opcion == '3':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
