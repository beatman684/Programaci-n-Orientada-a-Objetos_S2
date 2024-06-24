#PRUEBA EN PROCESO

class Libro:
    """
    Clase que representa un libro en la biblioteca.
    """
    def __init__(self, id_libro, titulo, autor, cantidad):
        self.id_libro = id_libro  # Identificador del libro
        self.titulo = titulo      # Título del libro
        self.autor = autor        # Autor del libro
        self.cantidad = cantidad  # Cantidad de copias disponibles

    def __str__(self):
        return f"Libro {self.id_libro}: {self.titulo} por {self.autor} (Cantidad: {self.cantidad})"

    def actualizar_cantidad(self, cantidad):
        """
        Actualiza la cantidad de copias disponibles del libro.
        """
        self.cantidad += cantidad


class Miembro:
    """
    Clase que representa un miembro de la biblioteca.
    """
    def __init__(self, id_miembro, nombre, email):
        self.id_miembro = id_miembro  # Identificador del miembro
        self.nombre = nombre          # Nombre del miembro
        self.email = email            # Email del miembro

    def __str__(self):
        return f"Miembro {self.id_miembro}: {self.nombre} (Email: {self.email})"


class Prestamo:
    """
    Clase que representa un préstamo de un libro a un miembro.
    """
    def __init__(self, miembro, libro, fecha_prestamo, fecha_devolucion):
        self.miembro = miembro               # Miembro que realiza el préstamo
        self.libro = libro                   # Libro prestado
        self.fecha_prestamo = fecha_prestamo # Fecha del préstamo
        self.fecha_devolucion = fecha_devolucion # Fecha de devolución

    def __str__(self):
        return (f"Préstamo:\nMiembro: {self.miembro.nombre}\nLibro: {self.libro.titulo}\n"
                f"Fecha de Préstamo: {self.fecha_prestamo}\nFecha de Devolución: {self.fecha_devolucion}")


class Biblioteca:
    """
    Clase que representa la biblioteca.
    """
    def __init__(self, nombre):
        self.nombre = nombre        # Nombre de la biblioteca
        self.libros = {}            # Diccionario de libros disponibles
        self.miembros = {}          # Diccionario de miembros registrados
        self.prestamos = []         # Lista de préstamos realizados

    def agregar_libro(self, libro):
        """
        Agrega un nuevo libro a la biblioteca.
        """
        self.libros[libro.id_libro] = libro

    def registrar_miembro(self, miembro):
        """
        Registra un nuevo miembro en la biblioteca.
        """
        self.miembros[miembro.id_miembro] = miembro

    def hacer_prestamo(self, id_miembro, id_libro, fecha_prestamo, fecha_devolucion):
        """
        Realiza un nuevo préstamo si el libro está disponible.
        """
        miembro = self.buscar_miembro(id_miembro)
        libro = self.buscar_libro(id_libro)
        if miembro and libro and libro.cantidad > 0:
            prestamo = Prestamo(miembro, libro, fecha_prestamo, fecha_devolucion)
            self.prestamos.append(prestamo)
            libro.actualizar_cantidad(-1)
            print(f"Préstamo realizado con éxito:\n{prestamo}")
        else:
            print(f"El préstamo no se pudo realizar. Verifique la disponibilidad del libro o los datos del miembro.")

    def buscar_libro(self, id_libro):
        """
        Busca un libro por su ID.
        """
        return self.libros.get(id_libro)

    def buscar_miembro(self, id_miembro):
        """
        Busca un miembro por su ID.
        """
        return self.miembros.get(id_miembro)

    def __str__(self):
        libros_str = "\n".join(str(l) for l in self.libros.values())
        miembros_str = "\n".join(str(m) for m in self.miembros.values())
        return f"Biblioteca {self.nombre}\n\nLibros disponibles:\n{libros_str}\n\nMiembros registrados:\n{miembros_str}"
