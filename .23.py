# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 10:55:07 2025

@author: lab
"""

import tkinter as tk
from tkinter import messagebox

# Función para abrir una ventana emergente
def abrir_emergente():
    # Crear una nueva ventana emergente (Toplevel)
    ventana_popup = tk.Toplevel(ventana)
    ventana_popup.title("Ventana Emergente")
    ventana_popup.geometry("300x150")

    # Etiqueta dentro de la ventana emergente
    etiqueta_popup = tk.Label(ventana_popup, text="¡Esta es una ventana emergente!", font=("Arial", 12))
    etiqueta_popup.pack(pady=20)

    # Botón para cerrar la ventana emergente
    boton_cerrar = tk.Button(ventana_popup, text="Cerrar", command=ventana_popup.destroy)
    boton_cerrar.pack(pady=10)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana Principal")
ventana.geometry("400x200")

# Botón para abrir la ventana emergente
boton_abrir = tk.Button(ventana, text="Abrir Ventana Emergente", command=abrir_emergente, font=("Arial", 12))
boton_abrir.pack(pady=60)

# Ejecutar la ventana
ventana.mainloop()
