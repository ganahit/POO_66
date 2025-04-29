# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 10:41:30 2025

@author: lab
"""
import tkinter as tk

# Función para cambiar el color de fondo de la ventana
def cambiar_color(color):
    ventana.config(bg=color)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cambiar Color de la Ventana")
ventana.geometry("300x200")

# Crear botones para cambiar el color
colores = ["red", "green", "blue", "yellow", "pink", "cyan", "orange", "purple"]

for color in colores:
    boton = tk.Button(ventana, text=f"{color.capitalize()}", bg=color, command=lambda c=color: cambiar_color(c))
    boton.pack(fill=tk.X, padx=10, pady=5)

# Ejecutar la ventana
ventana.mainloop()

