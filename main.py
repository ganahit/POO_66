# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 09:35:34 2025

@author: lab
"""

from modelos import (
    Arbol, Pelicula, Cine, Animal, Coche, DispositivoIoT,
    Robot, RedSocial, Antena, Mascota, Libro, SeguidorLinea,
    Router, PuntoAcceso
)

# Instancias y demostración

arbol = Arbol("Roble", 5, 10)
arbol.crecer(2)
arbol.fotosintesis()

pelicula = Pelicula("Inception", "Christopher Nolan", 148, "Ciencia Ficción")
pelicula.reproducir()

cine = Cine("Cinepolis", "Centro")
cine.agregar_pelicula(pelicula)
cine.mostrar_cartelera()

animal = Animal("Perro", 3, "guau")
animal.hacer_sonido()

coche = Coche("Toyota", "Corolla", "Gasolina")
coche.encender()
coche.conducir()

iot = DispositivoIoT("Lámpara", "Luz")
iot.encender()
iot.apagar()

robot = Robot("R2-D2", "limpiar")
robot.ejecutar_tarea()

red = RedSocial("Instagram", [])
red.registrar_usuario("usuario123")

antena = Antena(98.5, "Ciudad")
antena.transmitir()

mascota = Mascota("Luna", "Gato")
mascota.jugar()

libro = Libro("1984", "George Orwell", 328)
libro.leer()

seguidor = SeguidorLinea(10, 2)
seguidor.seguir_linea()

router = Router("TP-Link", "192.168.0.1")
router.conectar_dispositivo("Laptop")

punto = PuntoAcceso("MiWifi", 6)
punto.activar()
punto.desactivar()
