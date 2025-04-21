# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 09:34:42 2025

@author: lab
"""


class Arbol:
    def __init__(self, especie, altura, edad):
        self.especie = especie
        self.altura = altura
        self.edad = edad

    def crecer(self, metros):
        self.altura += metros
        print(f"El {self.especie} ha crecido {metros} metros. Ahora mide {self.altura} metros.")

    def fotosintesis(self):
        print(f"El {self.especie} está realizando fotosíntesis.")

class Pelicula:
    def __init__(self, titulo, director, duracion, genero):
        self.titulo = titulo
        self.director = director
        self.duracion = duracion
        self.genero = genero

    def reproducir(self):
        print(f"Reproduciendo la película '{self.titulo}'.")

    def obtener_info(self):
        return f"{self.titulo}, dirigida por {self.director}, Género: {self.genero}"

class Cine:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.cartelera = []

    def agregar_pelicula(self, pelicula):
        self.cartelera.append(pelicula)

    def mostrar_cartelera(self):
        print(f"Cartelera del cine {self.nombre}:")
        for peli in self.cartelera:
            print(peli.obtener_info())

class Animal:
    def __init__(self, especie, edad, sonido):
        self.especie = especie
        self.edad = edad
        self.sonido = sonido

    def hacer_sonido(self):
        print(f"El {self.especie} hace {self.sonido}.")

class Coche:
    def __init__(self, marca, modelo, combustible):
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
        self.encendido = False

    def encender(self):
        self.encendido = True
        print("Coche encendido.")

    def conducir(self):
        if self.encendido:
            print(f"Conduciendo el {self.marca} {self.modelo}.")
        else:
            print("El coche está apagado.")

class DispositivoIoT:
    def __init__(self, nombre, tipo, estado=False):
        self.nombre = nombre
        self.tipo = tipo
        self.estado = estado

    def encender(self):
        self.estado = True
        print(f"{self.nombre} encendido.")

    def apagar(self):
        self.estado = False
        print(f"{self.nombre} apagado.")

class Robot:
    def __init__(self, nombre, tarea):
        self.nombre = nombre
        self.tarea = tarea

    def ejecutar_tarea(self):
        print(f"{self.nombre} está ejecutando la tarea: {self.tarea}")

class RedSocial:
    def __init__(self, nombre, usuarios):
        self.nombre = nombre
        self.usuarios = usuarios

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario {usuario} registrado en {self.nombre}.")

class Antena:
    def __init__(self, frecuencia, ubicacion):
        self.frecuencia = frecuencia
        self.ubicacion = ubicacion

    def transmitir(self):
        print(f"Transmitiendo en {self.frecuencia} MHz desde {self.ubicacion}.")

class Mascota:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def jugar(self):
        print(f"{self.nombre} está jugando.")

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def leer(self):
        print(f"Estás leyendo '{self.titulo}' de {self.autor}.")

class SeguidorLinea:
    def __init__(self, velocidad, sensores):
        self.velocidad = velocidad
        self.sensores = sensores

    def seguir_linea(self):
        print("Siguiendo la línea...")

class Router:
    def __init__(self, modelo, ip, dispositivos_conectados=None):
        self.modelo = modelo
        self.ip = ip
        self.dispositivos_conectados = dispositivos_conectados or []

    def conectar_dispositivo(self, dispositivo):
        self.dispositivos_conectados.append(dispositivo)
        print(f"Dispositivo {dispositivo} conectado al router {self.modelo}.")

class PuntoAcceso:
    def __init__(self, ssid, canal, activo=False):
        self.ssid = ssid
        self.canal = canal
        self.activo = activo

    def activar(self):
        self.activo = True
        print(f"Punto de acceso {self.ssid} activado.")

    def desactivar(self):
        self.activo = False
        print(f"Punto de acceso {self.ssid} desactivado.")
