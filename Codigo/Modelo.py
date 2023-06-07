import tensorflow as tf
import numpy as np
import random
from keras import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.optimizers import Adam
from keras.utils import load_img, img_to_array


class Modelo:

    # El constructor recibe 5 datos, todos se inicializan por defecto pero pueden modificarse segun la necesidad.
    def __init__(self, formato_entrada=(100, 100, 1), formato_salida=3, optimizador='adam', bache=32, epocas=100):
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
        self.arquitectura = Sequential()
        self.arquitectura.add(Conv2D(32, (3,3), activation='relu', input_shape=(64, 64, 3)))
        self.arquitectura.add(MaxPooling2D((2,2)))
        self.arquitectura.add(Conv2D(64, (3,3), activation='relu'))
        self.arquitectura.add(MaxPooling2D((2,2)))
        self.arquitectura.add(Conv2D(128, (3,3), activation='relu'))
        self.arquitectura.add(MaxPooling2D((2,2)))
        self.arquitectura.add(Flatten())
        self.arquitectura.add(Dense(128, activation='relu'))
        self.arquitectura.add(Dense(3, activation='softmax'))

        # Compilamos el modelo para utilizarlo en el entrenador.
        self.compilar()

        # El resumen muestra como quedo la arquitectura de nuestro modelo:
        self.resumen()

    def compilar(self):
        self.arquitectura.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

    def resumen(self):
        self.arquitectura.summary()

    def predecir(self, archivo):
        x = load_img(archivo, target_size=(64, 64))
        x = img_to_array(x)
        x = np.expand_dims(x, axis=0)
        x = x / 255.0  # Normalizar la imagen.
        porcentajes = self.arquitectura.predict(x)
        print(type(porcentajes))
        print(porcentajes)
        resultado = porcentajes[0]
        prediccion = np.argmax(resultado)
        if prediccion == 0:
            prediccion = "CIRCULO"
            print("prediccion: Circulo")
        elif prediccion == 1:
            prediccion = "CUADRADO"
            print("prediccion: Cuadrado")
        elif prediccion == 2:
            prediccion = "TRIANGULO"
            print("prediccion: Triangulo")

        return porcentajes, prediccion
