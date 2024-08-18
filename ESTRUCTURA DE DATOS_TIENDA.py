#INICIANDO SECUENCIA DE COMANDOS
#ESTRUCUTURA DE DATOS_MI TIENDA_INGRRESO/ACTUALIZACION/ELIMINCION DE PRODUCTOS

# Clase Producto para representar cada producto en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto  # ID único para identificar el producto
        self._nombre = nombre  # Nombre del producto
        self._cantidad = cantidad  # Cantidad disponible del producto
        self._precio = precio  # Precio del producto

    # Getters y Setters para acceder y modificar los atributos del producto
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: {self._precio}"


# Clase Inventario para gestionar la colección de productos
class Inventario:
    def __init__(self):
        self._productos = []  # Lista de productos en el inventario

    def añadir_producto(self, producto):
        # Verifica que el ID sea único antes de añadir el producto
        if not any(p.get_id() == producto.get_id() for p in self._productos):
            self._productos.append(producto)
            print(f"Producto {producto.get_nombre()} añadido al inventario.")
        else:
            print(f"Error: Ya existe un producto con el ID {producto.get_id()}.")

    def eliminar_producto(self, id_producto):
        # Busca y elimina el producto por su ID
        producto_encontrado = None
        for producto in self._productos:
            if producto.get_id() == id_producto:
                producto_encontrado = producto
                break

        if producto_encontrado:
            self._productos.remove(producto_encontrado)
            print(f"Producto con ID {id_producto} eliminado del inventario.")
        else:
            print(f"Error: No se encontró un producto con ID {id_producto}.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        # Busca el producto por su ID y actualiza su cantidad o precio
        for producto in self._productos:
            if producto.get_id() == id_producto:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                print(f"Producto con ID {id_producto} actualizado.")
                return
        print(f"Error: No se encontró un producto con ID {id_producto}.")

    def buscar_producto_por_nombre(self, nombre):
        # Busca y retorna los productos con nombres similares
        productos_encontrados = [p for p in self._productos if nombre.lower() in p.get_nombre().lower()]
        if productos_encontrados:
            for producto in productos_encontrados:
                print(producto)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    def mostrar_inventario(self):
        # Muestra todos los productos en el inventario
        if self._productos:
            for producto in self._productos:
                print(producto)
        else:
            print("El inventario está vacío.")


# Interfaz de usuario en la consola
def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            nueva_cantidad = input("Ingrese la nueva cantidad (o presione Enter para omitir): ")
            nuevo_precio = input("Ingrese el nuevo precio (o presione Enter para omitir): ")
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            print("Saliendo del sistema de gestión de inventario.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


# Ejecutar el menú de gestión de inventario
if __name__ == "__main__":
    menu()
