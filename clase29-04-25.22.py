# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 10:54:14 2025

@author: lab
"""

import tkinter as tk

# Función para actualizar el texto de la etiqueta dinámica
def actualizar_texto():
    etiqueta_dinamica.config(text="¡El texto ha sido actualizado!", fg=entrada_color.get())

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Etiquetas Estáticas y Dinámicas")
ventana.geometry("450x300")

# Crear una etiqueta estática
etiqueta_estatica = tk.Label(ventana, text="Esta es una etiqueta estática", font=("Arial", 14))
etiqueta_estatica.pack(pady=10)

# Crear una etiqueta dinámica
etiqueta_dinamica = tk.Label(ventana, text="Texto inicial", font=("Arial", 14), fg="blue")
etiqueta_dinamica.pack(pady=10)

# Campo de entrada para personalizar el color
entrada_color = tk.Entry(ventana, font=("Arial", 14), fg="gray")
entrada_color.insert(0, "green")  # Valor predeterminado
entrada_color.pack(pady=10)

# Botón para actualizar la etiqueta dinámica
boton_actualizar = tk.Button(ventana, text="Actualizar Etiqueta Dinámica", command=actualizar_texto)
boton_actualizar.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
