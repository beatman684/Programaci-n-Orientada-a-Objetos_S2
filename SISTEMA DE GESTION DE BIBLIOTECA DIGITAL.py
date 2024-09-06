#INICIANDO SECUENCIA DE COMANDOS
#PROGRAMA PARA BIBLIOTECA DIGITAL

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
        self.info = (self.autor, self.titulo)

    def __str__(self):
        return f"{self.titulo} de {self.autor} (Categoría: {self.categoria}, ISBN: {self.isbn})"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        for libro in self.libros_prestados:
            if libro.isbn == isbn:
                self.libros_prestados.remove(libro)
                return libro
        return None

    def listar_libros_prestados(self):
        if self.libros_prestados:
            print(f"Libros prestados por {self.nombre}:")
            for libro in self.libros_prestados:
                print(f" - {libro}")
        else:
            print(f"{self.nombre} no tiene libros prestados.")


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.ids_usuarios = set()

    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print("Este libro ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"No se encontró el libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print("Este ID de usuario ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario {usuario.nombre} registrado exitosamente.")

    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario con ID {id_usuario} eliminado.")
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros.pop(isbn)
            usuario.prestar_libro(libro)
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            libro = usuario.devolver_libro(isbn)
            if libro:
                self.libros[isbn] = libro
                print(f"Libro '{libro.titulo}' devuelto a la biblioteca.")
            else:
                print(f"El usuario no tiene el libro con ISBN {isbn} en préstamo.")
        else:
            print("Usuario no encontrado.")

    def buscar_por_titulo(self, titulo):
        libros_encontrados = [libro for libro in self.libros.values() if titulo.lower() in libro.titulo.lower()]
        self.mostrar_libros_encontrados(libros_encontrados)

    def buscar_por_autor(self, autor):
        libros_encontrados = [libro for libro in self.libros.values() if autor.lower() in libro.autor.lower()]
        self.mostrar_libros_encontrados(libros_encontrados)

    def buscar_por_categoria(self, categoria):
        libros_encontrados = [libro for libro in self.libros.values() if categoria.lower() in libro.categoria.lower()]
        self.mostrar_libros_encontrados(libros_encontrados)

    def mostrar_libros_encontrados(self, libros_encontrados):
        if libros_encontrados:
            print("Libros encontrados:")
            for libro in libros_encontrados:
                print(f" - {libro}")
        else:
            print("No se encontraron libros con esos criterios.")


# Función para mostrar el menú principal
def mostrar_menu():
    print("\n=== Menú de la Biblioteca ===")
    print("1. Registrar usuario")
    print("2. Añadir libro")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Buscar libro")
    print("6. Listar libros prestados por usuario")
    print("7. Salir")
    return input("Selecciona una opción: ")


# Función principal para interactuar con el menú
def iniciar_biblioteca():
    biblioteca = Biblioteca()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            nombre = input("Introduce el nombre del usuario: ")
            id_usuario = input("Introduce el ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "2":
            titulo = input("Introduce el título del libro: ")
            autor = input("Introduce el autor del libro: ")
            categoria = input("Introduce la categoría del libro: ")
            isbn = input("Introduce el ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(libro)

        elif opcion == "3":
            id_usuario = input("Introduce el ID del usuario que quiere el préstamo: ")
            isbn = input("Introduce el ISBN del libro a prestar: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "4":
            id_usuario = input("Introduce el ID del usuario que devuelve el libro: ")
            isbn = input("Introduce el ISBN del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "5":
            print("Opciones de búsqueda: ")
            print("1. Por título")
            print("2. Por autor")
            print("3. Por categoría")
            tipo_busqueda = input("Selecciona una opción: ")

            if tipo_busqueda == "1":
                titulo = input("Introduce el título: ")
                biblioteca.buscar_por_titulo(titulo)
            elif tipo_busqueda == "2":
                autor = input("Introduce el autor: ")
                biblioteca.buscar_por_autor(autor)
            elif tipo_busqueda == "3":
                categoria = input("Introduce la categoría: ")
                biblioteca.buscar_por_categoria(categoria)
            else:
                print("Opción no válida.")

        elif opcion == "6":
            id_usuario = input("Introduce el ID del usuario: ")
            if id_usuario in biblioteca.usuarios:
                usuario = biblioteca.usuarios[id_usuario]
                usuario.listar_libros_prestados()
            else:
                print("Usuario no encontrado.")

        elif opcion == "7":
            print("Saliendo del sistema de biblioteca. ¡Hasta luego!")
            break

        else:
            print("Opción no válida, por favor intenta de nuevo.")


# Punto de entrada principal
if __name__ == "__main__":
    iniciar_biblioteca()
