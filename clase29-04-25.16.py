# -*- coding: utf-8 -*-
import tkinter as tk

# Función para cambiar el color de fondo de la ventana
def cambiar_color():
    color = entrada_color.get()
    try:
        ventana.config(bg=color)
    except Exception as e:
        resultado.config(text="Color no válido", fg="red")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cambiar Color de la Ventana")
ventana.geometry("300x200")

# Crear un campo de entrada para ingresar el color
tk.Label(ventana, text="Escribe un color o código hexadecimal:").pack(pady=10)
entrada_color = tk.Entry(ventana, font=("Arial", 12))
entrada_color.pack(pady=5)

# Botón para cambiar el color
tk.Button(ventana, text="Cambiar Color", command=cambiar_color).pack(pady=10)

# Etiqueta para mostrar mensajes de error
resultado = tk.Label(ventana, text="", font=("Arial", 10))
resultado.pack()

# Ejecutar la ventana
ventana.mainloop()
