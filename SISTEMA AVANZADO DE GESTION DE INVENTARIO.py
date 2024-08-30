#INICIANDO SECUENCIA DE COMANDOS
#GESTION DE INVENTARIO_FUNDAMENTOS DE COLECCIONES

import json


class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        self.producto_id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_producto_id(self):
        return self.producto_id

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_precio(self, precio):
        self.precio = precio

    def to_dict(self):
        return {
            "producto_id": self.producto_id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }


class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos con ID como clave

    def agregar_producto(self, producto):
        self.productos[producto.obtener_producto_id()] = producto
        print(f'Producto {producto.obtener_nombre()} agregado al inventario.')

    def eliminar_producto(self, producto_id):
        if producto_id in self.productos:
            del self.productos[producto_id]
            print(f'Producto ID {producto_id} eliminado del inventario.')
        else:
            print('Producto no encontrado.')

    def actualizar_producto(self, producto_id, cantidad=None, precio=None):
        if producto_id in self.productos:
            producto = self.productos[producto_id]
            if cantidad is not None:
                producto.establecer_cantidad(cantidad)
            if precio is not None:
                producto.establecer_precio(precio)
            print(f'Producto ID {producto_id} actualizado.')
        else:
            print('Producto no encontrado.')

    def buscar_producto(self, nombre):
        encontrados = [producto for producto in self.productos.values() if
                       nombre.lower() in producto.obtener_nombre().lower()]
        if encontrados:
            for producto in encontrados:
                print(
                    f'ID: {producto.obtener_producto_id()}, Nombre: {producto.obtener_nombre()}, Cantidad: {producto.obtener_cantidad()}, Precio: {producto.obtener_precio()}')
        else:
            print('No se encontraron productos con ese nombre.')

    def mostrar_inventario(self):
        print('Inventario:')
        for producto in self.productos.values():
            print(
                f'ID: {producto.obtener_producto_id()}, Nombre: {producto.obtener_nombre()}, Cantidad: {producto.obtener_cantidad()}, Precio: {producto.obtener_precio()}')

    def guardar_inventario(self, filename='inventario.json'):
        with open(filename, 'w') as file:
            json.dump({id: producto.to_dict() for id, producto in self.productos.items()}, file)
            print('Inventario guardado en archivo.')

    def cargar_inventario(self, filename='inventario.json'):
        try:
            with open(filename, 'r') as file:
                productos_data = json.load(file)
                for id, data in productos_data.items():
                    producto = Producto(data["producto_id"], data["nombre"], data["cantidad"], data["precio"])
                    self.agregar_producto(producto)
                print('Inventario cargado desde archivo.')
        except FileNotFoundError:
            print('No se encontró el archivo. Se iniciará un nuevo inventario.')


def menu():
    inventario = Inventario()
    inventario.cargar_inventario()  # Cargar el inventario al iniciar
    while True:
        print("\nMenú de Gestión de Inventario")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            nuevo_producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(nuevo_producto)

        elif opcion == '2':
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco si no se quiere actualizar): ")
            precio = input("Nuevo precio (dejar en blanco si no se quiere actualizar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_inventario()

        elif opcion == '6':
            inventario.guardar_inventario()

        elif opcion == '7':
            inventario.guardar_inventario()  # Guardar antes de salir
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
