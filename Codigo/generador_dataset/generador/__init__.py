import os
import turtle

from generador_dataset.generador.Figuras import *


class figurasGeometricas:
    generadores = [
        Triangulo, Circulo, Cuadrado
    ]

    def __init__(self, destino, tamanio, animacion=False):
        turtle.colormode(255)

        turtle.Screen().setup(200, 200)
        turtle.hideturtle()
        turtle.tracer(animacion)

        contenedor = turtle.Turtle()

        self.tamanio = tamanio
        self.figuras = [
            generador(
                destino, contenedor
            ) for generador in self.generadores
        ]

    def generar(self):
        contador = 1
        if not os.path.exists("imagenes"):
            os.makedirs("imagenes")
        for _ in range(self.tamanio):
            for figura in self.figuras:
                figura.generar(contador)
                contador += 1
