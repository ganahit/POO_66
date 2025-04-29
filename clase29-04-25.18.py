# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 10:44:41 2025

@author: lab
"""
import tkinter as tk

def copiar_texto():
    # Obtener el texto del cuadro de texto de entrada
    texto = cuadro_entrada.get("1.0", tk.END)
    # Poner el texto en el cuadro de texto de salida
    cuadro_salida.delete("1.0", tk.END)
    cuadro_salida.insert(tk.END, texto)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cuadros de Texto")
ventana.geometry("400x300")

# Etiqueta para cuadro de texto de entrada
tk.Label(ventana, text="Escribe algo en el cuadro de texto:").pack(pady=10)

# Crear un cuadro de texto de entrada
cuadro_entrada = tk.Text(ventana, height=5, width=40, font=("Arial", 12))
cuadro_entrada.pack(pady=10)

# Botón para copiar el texto
tk.Button(ventana, text="Copiar al cuadro de salida", command=copiar_texto).pack(pady=5)

# Etiqueta para cuadro de texto de salida
tk.Label(ventana, text="Texto copiado:").pack(pady=10)

# Crear un cuadro de texto de salida (solo lectura)
cuadro_salida = tk.Text(ventana, height=5, width=40, font=("Arial", 12), state=tk.DISABLED)
cuadro_salida.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()

