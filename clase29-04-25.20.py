# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 10:46:43 2025

@author: lab
"""

import tkinter as tk

# Función para actualizar el texto de la etiqueta dinámica
def actualizar_texto():
    etiqueta_dinamica.config(text="¡El texto ha sido actualizado!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Etiquetas Dinámicas")
ventana.geometry("350x250")

# Crear una etiqueta dinámica
etiqueta_dinamica = tk.Label(ventana, text="Este texto cambiará", font=("Arial", 14), fg="blue")
etiqueta_dinamica.pack(pady=10)

# Botón para actualizar el texto de la etiqueta dinámica
boton_actualizar = tk.Button(ventana, text="Actualizar Texto", command=actualizar_texto)
boton_actualizar.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
