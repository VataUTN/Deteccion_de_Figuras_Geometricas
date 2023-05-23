import tensorflow as tf
import os


class Entrenador:
    def __init__(self, modelo, imagenes_entrenamiento, etiquetas_entrenamiento):
        self.modelo = modelo
        self.imagenes_entrenamiento = imagenes_entrenamiento
        self.etiquetas_entrenamiento = etiquetas_entrenamiento

    def entrenar(self):
        ruta_modelo = os.path.join("ModeloEntrenado.h5")
        # Comprobar si el archivo que contiene el modelo entrenado existe.
        if os.path.isfile(ruta_modelo):
            # Cargar el modelo entrenado:
            modelo_entrenado = tf.keras.models.load_model(str(ruta_modelo))
            print('Modelo existente cargado desde archivo.')
            return modelo_entrenado
        else:
            # Si el archivo no existe, se entrena el modelo y se guarda:
            self.modelo.arquitectura.fit(
                self.imagenes_entrenamiento,
                self.etiquetas_entrenamiento,
                epochs=self.modelo.epocas,
                batch_size=self.modelo.bache,
                verbose=True)

            # Guardar el modelo entrenado:
            self.modelo.arquitectura.save('ModeloEntrenado.h5')
            print('Modelo entrenado y guardado en archivo.')