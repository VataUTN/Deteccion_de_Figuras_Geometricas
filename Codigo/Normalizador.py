import os
from PIL import Image
import re
import numpy as np
from keras.utils import to_categorical

def normalizar_imagen(ruta_imagen, ruta):
    global imagen_normalizada

    # Abre la imagen especificada por ruta_imagen.
    # 'with' se utiliza para garantizar que el archivo se cierre correctamente después de su uso.
    with Image.open(ruta_imagen) as imagen:

        # Convierte la imagen original a escala de grises.
        imagen_en_grises = imagen.convert("L")

        # Determina el tamaño objetivo manteniendo el aspecto original.
        ancho, alto = imagen_en_grises.size                                         # Obtengo dimensiones originales de la imagen
        relacion_aspecto = ancho / alto                                             # Calculo la relación de aspecto dividiendo el ancho entre el alto.
        ancho_objetivo = 100                                                        # Establezco un ancho objetivo deseado de 100 píxeles.
        alto_objetivo = int(ancho_objetivo / relacion_aspecto)                      # Calculo el alto objetivo utilizando la relación de aspecto y el ancho objetivo.
        imagen_redimensionada = imagen_en_grises.resize((ancho_objetivo, alto_objetivo))    #Redimensiono la imagen a las dimensiones objetivo.

        # Obtengo el color de fondo de la imagen original
        color_de_fondo = imagen.getpixel((1, 1))
        color_str = '#{:02x}{:02x}'.format(*color_de_fondo)
        # Crea una imagen normalizada con el mismo color de fondo que la imagen original
        imagen_normalizada = Image.new("L", (ancho_objetivo, 100), (color_str))

        # Calcula las coordenadas de la esquina superior izquierda para pegar la imagen redimensionada
        left = 0
        top = int((100 - alto_objetivo) / 2)

        # Pega la imagen redimensionada en la imagen normalizada
        imagen_normalizada.paste(imagen_redimensionada, (left, top))

        # Extrae el nombre de archivo de la ruta completa de la imagen original, divide el nombre de archivo en el nombre base y la extensión y se concatena ".png" para asegurarse de que la imagen normalizada tenga la extensión ".png"
        nombre_archivo_imagen_normalizada = os.path.splitext(os.path.basename(ruta_imagen))[0] + ".png"

        # Combina la ruta del directorio ruta con el nombre de archivo nombre_archivo_imagen_normalizada para crear la ruta completa de la imagen normalizada.
        ruta_imagen_normalizada = os.path.join(ruta, nombre_archivo_imagen_normalizada)

        # Guardo la imagen en disco.
        imagen_normalizada.save(ruta_imagen_normalizada, "PNG")

    return imagen_normalizada

def leerImagenesEnCarpeta(ruta_original, ruta_normalizada):
    imagenes_normalizadas = []
    for archivo in os.listdir(ruta_original):
        if archivo.endswith(".jpg") or archivo.endswith(".png"):
            imagen_original_path = os.path.join(ruta_original, archivo)
            imagen_normalizada = normalizar_imagen(imagen_original_path, ruta_normalizada)
            imagenes_normalizadas.append(imagen_normalizada)
    return imagenes_normalizadas

def cargar_imagenes_y_etiquetas(ruta):
    imagenes = []
    etiquetas = []
    for archivo in os.listdir(ruta):
        if archivo.endswith(".png"):
            match = re.match(r"([a-zA-Z]+)_([0-9]+)\.png", archivo)
            if match:
                forma = match.group(1)
                etiquetas.append(forma)

                imagen_path = os.path.join(ruta, archivo)
                imagen = np.asarray(Image.open(imagen_path))
                imagenes.append(imagen)

    label_mapping = {'Circulo': 0, 'Triangulo': 1, 'Cuadrado': 2}
    etiquetas_numericas = [label_mapping[etiqueta] for etiqueta in etiquetas]
    etiquetas = to_categorical(etiquetas_numericas, num_classes=3)

    return np.array(imagenes), etiquetas



def Analizar(ruta_original, ruta_normalizada):
    global imagen_normalizada
    hay_archivos = False
    elementos = os.listdir(ruta_original)
    for elemento in elementos:
        ruta_elemento = os.path.join(ruta_original, elemento)
        if os.path.isfile(ruta_elemento):
            hay_archivos = True
            break
    if hay_archivos == True:
        for archivo in os.listdir(ruta_original):
            imagen_original_path = os.path.join(ruta_original, archivo)
            for archivo in os.listdir(ruta_normalizada):
                os.remove(os.path.join(ruta_normalizada, archivo))
            imagen_normalizada = normalizar_imagen(imagen_original_path, ruta_normalizada)
            os.remove(imagen_original_path)
    else:
        for archivo in os.listdir(ruta_normalizada):
            imagen_normalizada = Image.open(os.path.join(ruta_normalizada, archivo))

    return imagen_normalizada

def normalizar(ruta_original, ruta_normalizada):

    # Verifico si no existe un directorio en la ruta especificada, si no existe, lo crea.
    if not os.path.exists(ruta_normalizada):
        os.makedirs(ruta_normalizada)

    imagenes_normalizadas = leerImagenesEnCarpeta(ruta_original, ruta_normalizada)
    print(f"Se han normalizado {len(imagenes_normalizadas)} imágenes y se han guardado en {ruta_normalizada}.")
