# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 10:43:47 2025

@author: lab
"""

import tkinter as tk

# Variable global para almacenar el color anterior
color_anterior = "white"  # Color inicial

# Función para cambiar el color de fondo de la ventana
def cambiar_color():
    global color_anterior  # Usamos la variable global para acceder al color anterior
    color = entrada_color.get()
    
    try:
        # Guardamos el color actual antes de cambiarlo
        color_anterior = ventana.cget("bg")
        ventana.config(bg=color)
        resultado.config(text="")
    except Exception as e:
        resultado.config(text="Color no válido", fg="red")

# Función para regresar al color anterior
def regresar_color():
    global color_anterior  # Usamos la variable global para acceder al color anterior
    ventana.config(bg=color_anterior)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cambiar Color de la Ventana")
ventana.geometry("300x250")

# Crear un campo de entrada para ingresar el color
tk.Label(ventana, text="Escribe un color o código hexadecimal:").pack(pady=10)
entrada_color = tk.Entry(ventana, font=("Arial", 12))
entrada_color.pack(pady=5)

# Botón para cambiar el color
tk.Button(ventana, text="Cambiar Color", command=cambiar_color).pack(pady=10)

# Botón para regresar al color anterior
tk.Button(ventana, text="Regresar al Color Anterior", command=regresar_color).pack(pady=5)

# Etiqueta para mostrar mensajes de error
resultado = tk.Label(ventana, text="", font=("Arial", 10))
resultado.pack()

# Ejecutar la ventana
ventana.mainloop()
