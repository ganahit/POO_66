# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 10:46:03 2025

@author: lab
"""
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Etiquetas Estáticas")
ventana.geometry("350x200")

# Crear una etiqueta estática
etiqueta_estatica_1 = tk.Label(ventana, text="Esta es una etiqueta estática", font=("Arial", 12))
etiqueta_estatica_1.pack(pady=10)

# Crear otra etiqueta estática
etiqueta_estatica_2 = tk.Label(ventana, text="Texto estático adicional", font=("Helvetica", 12, "italic"))
etiqueta_estatica_2.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()

