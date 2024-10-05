import tkinter as tk
from tkinter import messagebox

# Función para añadir una nueva tarea a la lista
def add_task(event=None):
    task = entry_task.get().strip()  # Obtiene la tarea del campo de entrada
    if task:  # Si la tarea no está vacía
        listbox_tasks.insert(tk.END, task)  # Añade la tarea al final de la lista
        entry_task.delete(0, tk.END)  # Limpia el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

# Función para marcar una tarea como completada
def complete_task(event=None):
    try:
        index = listbox_tasks.curselection()[0]  # Obtiene el índice de la tarea seleccionada
        task = listbox_tasks.get(index)  # Obtiene el texto de la tarea
        listbox_tasks.delete(index)  # Elimina la tarea de la lista
        listbox_tasks.insert(tk.END, f"[Completado] {task}")  # Añade la tarea como completada
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para marcar como completada.")

# Función para eliminar la tarea seleccionada
def delete_task(event=None):
    try:
        index = listbox_tasks.curselection()[0]  # Obtiene el índice de la tarea seleccionada
        listbox_tasks.delete(index)  # Elimina la tarea de la lista
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para eliminar.")

# Función para cerrar la aplicación
def close_app(event=None):
    window.quit()  # Cierra la ventana principal

# Crear la ventana principal
window = tk.Tk()
window.title("Gestor de Tareas con Atajos")

# Crear el campo de entrada para nuevas tareas
entry_task = tk.Entry(window, width=40)
entry_task.grid(row=0, column=0, padx=10, pady=10)

# Botón para añadir una nueva tarea
button_add_task = tk.Button(window, text="Añadir Tarea", command=add_task)
button_add_task.grid(row=0, column=1, padx=10, pady=10)

# Listbox para mostrar las tareas pendientes
listbox_tasks = tk.Listbox(window, width=50, height=10)
listbox_tasks.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Botón para marcar la tarea seleccionada como completada
button_complete_task = tk.Button(window, text="Completar Tarea", command=complete_task)
button_complete_task.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

# Botón para eliminar la tarea seleccionada
button_delete_task = tk.Button(window, text="Eliminar Tarea", command=delete_task)
button_delete_task.grid(row=2, column=1, padx=10, pady=10, sticky=tk.E)

# Vincular atajos de teclado
window.bind("<Return>", add_task)  # Añadir tarea con Enter
window.bind("<c>", complete_task)  # Marcar tarea como completada con "C"
window.bind("<Delete>", delete_task)  # Eliminar tarea con Delete
window.bind("<d>", delete_task)  # Eliminar tarea con "D"
window.bind("<Escape>", close_app)  # Cerrar la aplicación con Escape

# Ejecutar el bucle principal de la aplicación
window.mainloop()
