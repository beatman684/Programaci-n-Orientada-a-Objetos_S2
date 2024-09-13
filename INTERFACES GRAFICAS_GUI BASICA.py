#INICIANDO SECUENCIA DE COMANDOS
#PROGARMA BASICO DE INTERFACE GRAFICA

import tkinter as tk
from tkinter import ttk  # Para usar Treeview

# Función para agregar un elemento a la tabla
def agregar_dato():
    dato = entrada.get()  # Obtener el dato ingresado
    if dato:
        tabla.insert('', tk.END, values=(dato,))  # Insertar en la tabla
        entrada.delete(0, tk.END)  # Limpiar el campo de texto

# Función para limpiar la tabla
def limpiar_tabla():
    for item in tabla.get_children():
        tabla.delete(item)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.pack(pady=5)

# Campo de texto
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

# Botón "Agregar"
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Tabla para mostrar los datos
tabla = ttk.Treeview(ventana, columns=('Dato',), show='headings')
tabla.heading('Dato', text='Dato')
tabla.pack(pady=5)

# Botón "Limpiar"
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_tabla)
boton_limpiar.pack(pady=5)

# Iniciar el bucle principal de la GUI
ventana.mainloop()
