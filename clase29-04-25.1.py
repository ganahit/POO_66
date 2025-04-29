# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 09:57:12 2025

@author: lab
"""

import tkinter as tk

def mostrar_texto():
    texto = entrada.get()
    etiqueta.config(text=texto)

ventana = tk.Tk()
entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="click", command=mostrar_texto)
boton.pack(side=tk.LEFT)
marco = tk.Frame(ventana)
marco.pack
boton1 = tk.Button(ventana, text="click", command=mostrar_texto)
boton1.pack(side=tk.RIGHT)
boton.pack()
boton.configure(bg="#edbb99")

etiqueta = tk.Label(ventana, text="")
etiqueta.pack()
marco = tk.Frame(ventana)
marco.pack()
ventana.configure(bg="#DAF7A6")
ventana.mainloop()
