import tensorflow as tf
import os
from keras.callbacks import EarlyStopping
from keras.preprocessing.image import ImageDataGenerator


class Entrenador:

    # Directorios de los conjuntos de datos
    directorio_entrenamiento = 'data/entrenamiento'
    directorio_validacion = 'data/validacion'

    # Preprocesamiento de imágenes y generadores de datos
    entrenamiento_datagen = ImageDataGenerator(rescale=1.0 / 255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
    validacion_datagen = ImageDataGenerator(rescale=1.0 / 255)

    generador_entrenamiento = entrenamiento_datagen.flow_from_directory(
        directorio_entrenamiento,
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical'
    )
    generador_validacion = validacion_datagen.flow_from_directory(
        directorio_validacion,
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical'
    )

    # Definir early stopping
    early_stopping = EarlyStopping(monitor='val_loss', patience=15, restore_best_weights=True)
    def __init__(self, modelo):
        self.modelo = modelo

    def entrenar(self):
        ruta_modelo = os.path.join('./modelo/', 'modelo.h5')
        ruta_pesos = os.path.join('./modelo/', 'pesos.h5')
        # Comprobar si el archivo que contiene el modelo entrenado existe.
        if os.path.isfile(ruta_modelo):
            # Cargar el modelo entrenado:
            self.modelo.arquitectura = tf.keras.models.load_model(ruta_modelo)
            self.modelo.arquitectura.load_weights(ruta_pesos)
            print('Modelo existente cargado desde archivo.')
        else:
            # Si el archivo no existe, se entrena el modelo y se guarda:
            self.modelo.arquitectura.fit(
                self.generador_entrenamiento,
                epochs=self.modelo.epocas,
                validation_data=self.generador_validacion,
                callbacks=[self.early_stopping]
            )

            # Guardar el modelo y los pesos:
            if not os.path.exists('./modelo/'):
                os.mkdir('./modelo/')
            self.modelo.arquitectura.save('./modelo/modelo.h5')
            self.modelo.arquitectura.save_weights('./modelo/pesos.h5')
            print('Modelo entrenado y guardado en archivo.')
