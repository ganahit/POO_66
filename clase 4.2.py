# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 10:29:56 2025

@author: lab
"""

#poner un numero y que me refleje los 10 numeros primos por modulos
def es_primo(n):
    """Función que devuelve True si el número es primo, False si no lo es."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primeros_primos_a_partir_de(numero):
    """Genera los primeros 10 números primos mayores o iguales al número dado."""
    primos = []
    while len(primos) < 10:
        if es_primo(numero):
            primos.append(numero)
        numero += 1
    return primos

# Solicitar al usuario el número de inicio
numero_inicio = int(input("Introduce un número: "))

# Obtener los primeros 10 números primos a partir de ese número
primos = primeros_primos_a_partir_de(numero_inicio)

# Mostrar los resultados
print(f"Los primeros 10 números primos a partir de {numero_inicio} son: {primos}")
