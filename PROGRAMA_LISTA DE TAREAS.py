#INICIANDO SECUENCIA DE COMANDOS
#LISTA DE TAREAS_MANEJO DE EVENTOS

import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Por favor, ingresa una tarea.")

def complete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(selected_task_index, f"[Completada] {task}")
    except IndexError:
        messagebox.showwarning("Selecciona una tarea", "Por favor, selecciona una tarea para marcarla como completada.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selecciona una tarea", "Por favor, selecciona una tarea para eliminar.")

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")

# Crear widgets
entry = tk.Entry(root, width=40)
entry.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_button.grid(row=0, column=1, padx=10)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

complete_button = tk.Button(root, text="Marcar como Completada", command=complete_task)
complete_button.grid(row=2, column=0, padx=10, pady=10)

delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.grid(row=2, column=1, padx=10, pady=10)

# Eventos
entry.bind("<Return>", add_task)

# Iniciar el loop de la aplicación
root.mainloop()
