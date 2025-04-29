import tkinter as tk

# Función para agregar elementos a la lista con colores personalizados
def agregar_elemento():
    # Obtener el texto del cuadro de entrada
    elemento = entrada.get()
    color = entrada_color.get()  # Obtener el color de la entrada

    if elemento and color:  # Verificar que ambos campo estén llenos
        # Agregar el elemento a la lista de la caja de texto
        lista.insert(tk.END, elemento + "\n")
        # Obtener el índice del último elemento agregado
        index = lista.index(tk.END)  # Indice de la última línea
        # Aplicar el color especificado al texto de esa línea
        lista.tag_add(color, f"{index}-1c linestart", f"{index}-1c lineend")
        lista.tag_configure(color, foreground=color)  # Configurar el color del texto
        entrada.delete(0, tk.END)  # Limpiar la entrada de texto
        entrada_color.delete(0, tk.END)  # Limpiar el campo de color
    else:
        resultado.config(text="Por favor, ingrese un texto y un color", fg="red")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lista con Colores Personalizables")
ventana.geometry("450x350")

# Crear un cuadro de entrada para el texto
entrada = tk.Entry(ventana, font=("Arial", 14))
entrada.pack(pady=10)

# Crear un cuadro de entrada para el color
entrada_color = tk.Entry(ventana, font=("Arial", 14), fg="gray")
entrada_color.insert(0, "red")  # Valor predeterminado
entrada_color.pack(pady=10)

# Etiqueta para mostrar mensaje de error
resultado = tk.Label(ventana, text="", font=("Arial", 10))
resultado.pack()

# Crear un botón para agregar elementos
boton_agregar = tk.Button(ventana, text="Agregar Elemento", command=agregar_elemento)
boton_agregar.pack(pady=10)

# Crear un cuadro de texto para mostrar la lista
lista = tk.Text(ventana, height=10, width=40, font=("Arial", 12), wrap=tk.WORD)
lista.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
