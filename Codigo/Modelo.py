import tensorflow as tf
import numpy as np
import random
from keras import layers


class Modelo:

    # El constructor recibe 5 datos, todos se inicializan por defecto pero pueden modificarse segun la necesidad.
    def __init__(self, formato_entrada=(100, 100, 1), formato_salida=3, optimizador='adam', bache=32, epocas=10):
        self.formato_entrada = formato_entrada
        self.formato_salida = formato_salida
        self.optimizador = optimizador
        self.bache = bache                      # Tanto el bache como las epocas se utilizan en el entrenador.
        self.epocas = epocas

        # Semilla: la "semilla" se refiere a un número utilizado para inicializar los parámetros del modelo de forma pseudoaleatoria.
        # Esta semilla se utiliza para controlar la generación de números aleatorios y asegurar que los resultados sean reproducibles.
        # Establecer la semilla para TensorFlow.
        seed_value = 1138  # “Que la fuerza te acompañe.” – Obi-Wan Kenobi.
        tf.random.set_seed(seed_value)

        # Establecer la semilla para Python en general.
        random.seed(seed_value)

        # Establecer la semilla para NumPy.
        np.random.seed(seed_value)

        # Se crea un modelo secuencial vacío. El modelo secuencial es una pila lineal de capas.
        # Definimos la arquitectura de la red neuronal:
        self.arquitectura = tf.keras.Sequential([
            layers.Conv2D(32, (3, 3), activation='relu', input_shape=self.formato_entrada),     # Capa de Convolución y Entrada.
            layers.MaxPooling2D((2, 2)),                                                        # Capa de Submuestro/Pooling: Reduce la dimensionalidad de los mapas de características obtenidos de la capa de convolución anterior.
            layers.Conv2D(64, (3, 3), activation='relu'),                                       # Capa de Convolución.
            layers.MaxPooling2D((2, 2)),                                                        # Capa de Submuestro/Pooling.
            layers.Conv2D(64, (3, 3), activation='relu'),                                       # Capa de Convolución.
            layers.Flatten(),                                                                   # Capa de Aplanamiento: Para convertir una entrada multidimensional en una sola dimensión. Se usa para pasar un formato de matriz a un vector lineal.
            layers.Dense(64, activation='relu'),                                                # Capa Oculta: Es una capa densa(totalmente conectada), que realiza operaciones lineales y no lineales en los datos.
            layers.Dense(self.formato_salida, activation='softmax')                             # Capa de Salida.
        ])

        # Compilamos el modelo para utilizarlo en el entrenador.
        self.compilar()

        # El resumen muestra como quedo la arquitectura de nuestro modelo:
        self.resumen()

    def compilar(self):
        self.arquitectura.compile(optimizer=self.optimizador, loss='categorical_crossentropy', metrics=['accuracy'])

    def resumen(self):
        self.arquitectura.summary()
