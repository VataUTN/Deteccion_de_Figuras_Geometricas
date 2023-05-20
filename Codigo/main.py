import os
import subprocess
import sys
import UI.PaginaPrincipal as pag


def crear_directorios():
    if not os.path.exists("imagen_a_analizar"):
        os.makedirs("imagen_a_analizar")
    if not os.path.exists("imagenes_normalizadas"):
        os.makedirs("imagenes_normalizadas")
    if not os.path.exists("imagen_analizada"):
        os.makedirs("imagen_analizada")

def instalar_dependencias():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        print("Error al instalar las dependencias:")
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    # En caso de no existir, se crean los directorios necesarios.
    crear_directorios()

    # Instalamos las dependencias necesarias:
    instalar_dependencias()

    # Iniciar la UI:
    app = pag.App()