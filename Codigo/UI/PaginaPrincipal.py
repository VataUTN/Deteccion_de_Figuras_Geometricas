import os
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter.font import BOLD
from PIL import ImageTk, Image
import numpy as np
import cv2
from Codigo.Entrenador import Entrenador
from Codigo.Modelo import Modelo
from Codigo.Normalizador import cargar_imagenes_y_etiquetas


# Creando clase de la interfaz de usuario
class App:
    # Constructor
    def __init__(self):
        self.ventana = tk.Tk()  # Creo la ventana
        self.ventana.title("Reconocimiento de figuras")  # Le pongo titulo

        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()  # ancho y alto de la pantalla en píxeles

        #  %d se reemplaza por los valores de w y h.
        # +0+0 ubica la ventana en la parte superior izquierda de la pantalla
        self.ventana.geometry("%dx%d+0+0" % (w, h))                 # le doy dimensiones a la ventana.
        self.ventana.config(bg="#fcfcfc")                           # le doy color.
        self.ventana.resizable(False, False)                        # indico que no se pueda redimensionar.
        logo = self.leer_imagen(os.path.join("UI", "logo.png"), (200, 200))          # leo el logo con la funcion leer_imagen.
        self.ventana.iconbitmap(os.path.join("UI", "logo.png"))
        # Esto es para linux:
        # self.ventana.iconphoto(True, tk.PhotoImage(file="UI/logo.png"))

        # PANEL DEL LOGO A LA IZQUIERDA.
        # Contenedor, sin borde, ancho=600, relieve del borde:solido, padding horizontal:10, color de fondo.
        logo_contenedor = tk.Frame(self.ventana, bd=0, width=600, relief=tk.SOLID, bg='#35003F')

        # Ubico el contenedor en la ventana, en el lado derecho, no se expande a toda la ventana pero si rellena el espacio.
        logo_contenedor.pack(side="left", expand=tk.NO, fill=tk.BOTH)

        # AREA PARA EL LOGO.
        # Contenedor, mando el logo, color de fondo
        imagen = tk.Label(logo_contenedor, image=logo, bg='#35003F')

        # Coloco el area en el contenedor: x, y = coordenadas, relwidht, relheight = ancho y alto relativo al contenedor (ocupa el total).
        imagen.place(x=0, y=0, relwidth=1, relheight=1)

        # PANEL A LA DERECHA.
        # Contenedor, sin borde, relieve del borde:solido, color de fondo.
        contenedor = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')

        # Coloco el contenedor en la ventana, a la derecha, que si se expanda y rellene el espacio total sobrante.
        contenedor.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        # PANEL PARTE DE ARRIBA DEL PANEL DERECHO.
        # Contenedor, alto=100, sin borde, relieve del borde:solido, color de fondo.
        contenedor_arriba = tk.Frame(contenedor, height=100, bd=0, relief=tk.SOLID, bg='#fcfcfc')

        # ubico el contenedor en la parte de arriba, que rellene el espacio solo en el ancho
        contenedor_arriba.pack(side="top", fill=tk.X)

        # AREA PARA TITULO DE PANEL ARRIBA.
        # Contenedor, texto, tipografia, color de letra, color de fondo, relleno superior e inferior de 30.
        titulo = tk.Label(contenedor_arriba, text="Ingrese una imagen:", font=('Arial', 30), fg="#666a88", bg="#fcfcfc", pady=30)

        # Ubico el area en su contenedor, que rellene el total del espacio del contenedor.
        titulo.pack(expand=tk.YES, fill=tk.BOTH)

        # Inicializo atributos vacios.
        self.texto_imagen = None
        self.label_imagen = None
        self.texto_reconoce = None
        self.figura = None

        # PANEL PARTE DE ABAJO DEL PANEL DERECHO.
        # Contenedor, alto=50, sin borde, relieve del borde:solido, color de fondo.
        contenedor_abajo = tk.Frame(contenedor, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')

        # Ubico el contenedor en la parte de abajo, que se expanda y rellene.
        contenedor_abajo.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        # BOTON DE INGRESAR IMAGEN.
        # Crear botón para cargar imagen.
        # Contenedor, texto, tipografia, color de fondo, sin borde, color de letra.
        # Command=lambda: funcion que se llama cuando presiona el boton, se define donde se usa, le paso el contenedor.
        btn_cargar = tk.Button(contenedor_abajo, text="Cargar imagen", font=('Arial', 15, BOLD), bg="#35003F", bd=0, fg="#fff",
                               command=lambda: self.cargar_imagen(contenedor_abajo))

        # Ubico el boton en su contenedor.
        btn_cargar.pack(fill=tk.X, padx=20, pady=20)

        # Inicio bucle infinito para correr la ventana.
        self.ventana.mainloop()

    # Función para leer imagen:
    def leer_imagen(self, ruta, tamanio):  # recibe ruta y tamaño (ancho, alto).
        return ImageTk.PhotoImage(Image.open(ruta).resize(tamanio, Image.ANTIALIAS))
        # 1. Abre la imagen ubicada en la ruta usando Image.open(ruta).
        # 2. Redimensiona la imagen a las dimensiones de tamanio usando el método resize(size, Image.ANTIALIAS).
        # 3. Image.ANTIALIAS se utiliza para mejorar la calidad de la imagen redimensionada utilizando un algoritmo de suavizado.
        # 4. Se crea una instancia de ImageTk.PhotoImage con la imagen redimensionada y la devuelve.

    # Función del botón "cargar imagen".
    def cargar_imagen(self, contenedor_abajo):

        ruta_archivo = filedialog.askopenfilename()  # Hago que se abra la biblioteca, guardo ruta imagen ingresada.

        if not ruta_archivo:                    # Verificar si se seleccionó un archivo.
            messagebox.showerror("Error", "No se seleccionó ningún archivo.")
            return

        if self.label_imagen is not None:       # Si ya había una imagen en el area de la imagen, la destruye.
            self.label_imagen.destroy()

        if self.texto_imagen is not None:       # Si ya había un texto en el texto de la imagen, lo destruye.
            self.texto_imagen.destroy()

        # Cargar imagen utilizando PIL
        imagen = Image.open(ruta_archivo)
        imagen.thumbnail((200, 200))

        # Transformo la imagen a una PhotoImage para poder mostrarla en la interfaz.
        imagen_ingresada = ImageTk.PhotoImage(imagen)

        # Defino el texto que dice "imagen ingresada".
        self.texto_imagen = tk.Label(contenedor_abajo, text="Imagen ingresada:", font=('Arial', 14), fg="#666a88", bg="#fcfcfc", pady=30)
        self.texto_imagen.pack()

        # Crear widget Label para mostrar la imagen cargada.
        self.label_imagen = tk.Label(contenedor_abajo)  # Creo widget Label para mostrar la imagen cargada.
        self.label_imagen.pack()

        imagen.save("./imagen_a_analizar/imagen_ingresada.png")  # Guardar imagen en el proyecto.

        self.label_imagen.config(image=imagen_ingresada)  # Mostrar imagen en widget Label.
        self.label_imagen.image = imagen_ingresada

        self.reconoceFigura(contenedor_abajo)  # Llamo a funcion para reconocer figura.


    # TODO: REVISAR VINCULO ENTRE MODELO / ENTRENADOR / IMAGEN INGRESADA.
    def reconoceFigura(self, contenedor_abajo):

        if self.texto_reconoce is not None:         # Eliminar el widget Label existente si es que hay uno.
            self.texto_reconoce.destroy()

        if self.figura is not None:                 # Eliminar el widget Label del resultado si es que hay uno.
            self.figura.destroy()

        # imagen_normalizada = Normalizador.Analizar("imagen_a_analizar", "imagen_analizada")
        imagen = cv2.imread("imagen_a_analizar/imagen_ingresada.png")
        imagen_normalizada = cv2.resize(imagen, (100, 100))
        imagen_normalizada = cv2.cvtColor(imagen_normalizada, cv2.COLOR_BGR2GRAY)
        imagen_normalizada = imagen_normalizada.reshape(100, 100, 1)
        cv2.imwrite("./imagen_analizada/imagen_normalizada.png",
                    imagen_normalizada)  # Guardar la imagen en el directorio especificado

        imagenes, etiquetas = cargar_imagenes_y_etiquetas("imagenes_normalizadas")

        # Creo un objeto de la clase entrenador, dejo las propiedades por defecto.
        modelo = Modelo()
        entrenador = Entrenador(modelo, imagenes, etiquetas)

        # Llamo a la funcion entrenar.
        entrenador.entrenar()

        # Guardo resultado de la prediccion (numero 0-5).
        imagen_tensor = np.expand_dims(imagen_normalizada, axis=0)
        prediccion = entrenador.modelo.arquitectura.predict(imagen_tensor)

        # prediccion_red = np.around(prediccion, 2)
        # Guardo valores de cada resultado en un diccionario.
        figuras = {
            0: "CIRCULO",
            1: "TRIANGULO",
            2: "CUADRADO"
        }
        prediccion = np.around(prediccion.flatten(), 3)
        print('circulo', prediccion[0])
        print('triangulo', prediccion[1])
        print('cuadrado', prediccion[2])
        reconoce = False;
        m = prediccion[0]
        indice = 0
        # Guardo el indice de la figura que más cerca estuvo del 100%.
        for i in range(len(prediccion)):
            if prediccion[i] > 0.7:
                reconoce = True
                if prediccion[i] > m:
                    m = prediccion[i]
                    indice = i

        # Guardo en nombre_figura, el valor de la clave que predijo.
        nombre_figura = figuras[indice]

        if reconoce == True:
            self.texto_reconoce = tk.Label(contenedor_abajo, text="Es un:", font=('Arial', 14), fg="#666a88", bg="#fcfcfc", pady=30)

            # Creo un label que muestre el resultado de la predicción.
            self.figura = tk.Label(contenedor_abajo, text=f"FIGURA: {nombre_figura}", font=('Arial', 20), fg="black",
                                   bg="#3e7ff6", highlightbackground="black", highlightthickness=2, pady=30, padx=20)
        else:
            self.texto_reconoce = tk.Label(contenedor_abajo, text="", font=('Arial', 14), fg="#666a88", bg="#fcfcfc", pady=30)

            # Creo un label que muestre que no hubo predicción.
            self.figura = tk.Label(contenedor_abajo, text="No se ha reconocido ninguna figura.", font=('Arial', 20),
                                   fg="black",
                                   bg="#3e7ff6", highlightbackground="black", highlightthickness=2, pady=30, padx=20)

        self.texto_reconoce.pack()
        self.figura.pack()
