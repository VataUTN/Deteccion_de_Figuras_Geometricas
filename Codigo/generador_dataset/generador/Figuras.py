import io
import random
from abc import ABC, abstractmethod
from os import path

import numpy as np
from PIL import Image


class figuraAbstracta(ABC):

    def __init__(self, destino, pintor):
        self.romper = None
        self.pintor = pintor
        self.destino = destino
        self.radio = None
        self.x = None
        self.y = None

    def fondo_random(self):

        color_fondo = ((0, 0, 0), (0, 0, 128), (128, 0, 0))
        color_seleccionado = random.choice(color_fondo)
        color_str = '#{:02x}{:02x}{:02x}'.format(*color_seleccionado)
        self.pintor.fillcolor(color_str)
        self.pintor.color(color_str)
        self.pintor.penup()
        self.pintor.setposition(-160, 160)
        self.pintor.pendown()
        self.pintor.begin_fill()

        self.pintor.goto(160, 160)
        self.pintor.goto(160, -160)
        self.pintor.goto(-160, -160)
        self.pintor.goto(-160, 160)

        self.pintor.end_fill()
        self.pintor.penup()

    def parametros_random(self):

        self.pintor.reset()

        self.fondo_random()
        color = ((0, 255, 0), (0, 255, 255), (255, 255, 0))
        color_seleccionado = random.choice(color)
        color_str = '#{:02x}{:02x}{:02x}'.format(*color_seleccionado)
        self.pintor.fillcolor(color_str)
        self.pintor.fillcolor(color_str)
        self.pintor.penup()
        self.radio = np.random.randint(10, 75)
        self.rotacion = np.deg2rad(np.random.randint(-180, 180))

        self.x, self.y = (
            np.random.randint(
                -80 + self.radio,
                80 - self.radio
            ),
            np.random.randint(
                -80 + self.radio,
                80 - self.radio
            )
        )

    def guardar_dibujo(self, contador):

        ps = self.pintor.getscreen().getcanvas().postscript(
            colormode='color', pageheight=199, pagewidth=199
        )
        im = Image.open(io.BytesIO(ps.encode('utf-8')))
        im.save(path.join(
            self.destino,
            self.__class__.__name__ + "_" + str(contador) + '.png'
        ), quality=100, format='png')

    def generar(self, contador):
        self.parametros_random()
        self.dibujar()
        self.guardar_dibujo(contador)

    def dibujar(self):
        self.pintor.penup()
        coordenadas_figura = self.obtener_coordenadas_figura()
        coordenadas = []

        for item in coordenadas_figura:
            coordenadas.append(
                (
                    (item[0] - self.x) * np.cos(self.rotacion) -
                    (item[1] - self.y) * np.sin(self.rotacion) + self.x,

                    (item[0] - self.x) * np.sin(self.rotacion) +
                    (item[1] - self.y) * np.cos(self.rotacion) + self.y
                )
            )

        self.pintor.goto(coordenadas[-1])

        self.pintor.pendown()
        self.pintor.begin_fill()

        for idx, item in enumerate(coordenadas):
            self.pintor.goto(item)
            if self.romper and self.romper == idx:
                self.pintor.end_fill()
                self.pintor.begin_fill()

        self.pintor.end_fill()
        self.pintor.hideturtle()

    @abstractmethod
    def obtener_coordenadas_figura(self):
        raise NotImplementedError()


class poligonoAbstracto(figuraAbstracta, ABC):
    numero_de_vertices = None
    romper = None

    def obtener_coordenadas_figura(self):

        if not self.numero_de_vertices:
            raise NotImplementedError("El numero de vertice debe ser especificado en las subclases.")

        coordenadas = []
        for vertice in range(self.numero_de_vertices):
            coordenadas.append(
                (
                    self.radio * np.cos(
                        2 * np.pi * vertice / self.numero_de_vertices
                    ) + self.x,
                    self.radio * np.sin(
                        2 * np.pi * vertice / self.numero_de_vertices
                    ) + self.y
                )
            )
        return coordenadas


class Triangulo(poligonoAbstracto):
    numero_de_vertices = 3


class Cuadrado(poligonoAbstracto):
    numero_de_vertices = 4


class Circulo(figuraAbstracta):

    def dibujar(self):
        self.pintor.setposition(self.x, self.y - self.radio)

        self.pintor.pendown()
        self.pintor.begin_fill()
        self.pintor.ht()
        self.pintor.circle(self.radio)
        self.pintor.end_fill()

    def obtener_coordenadas_figura(self):
        pass
