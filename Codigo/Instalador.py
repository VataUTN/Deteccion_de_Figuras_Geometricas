import subprocess  # Importar el módulo subprocess para ejecutar comandos en el sistema operativo
import sys  # Importar el módulo sys para acceder a variables y funciones específicas del intérprete de Python

def instalar(nombre, comando):
    # Imprimir mensaje indicando la instalación en proceso:
    print(f"Instalando {nombre}...")

    # Ejecutar el comando y capturar el resultado:
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    verificarInstalacion(resultado)

def verificarInstalacion(resultado):
    # Verificar si el comando se ejecutó correctamente:
    if resultado.returncode == 0:
        # Imprimir la salida estándar del comando:
        print("La salida del comando es:")
        print(resultado.stdout)
    else:
        # Imprimir la salida de error del comando:
        print("Se produjo un error al ejecutar el comando:")
        print(resultado.stderr)

def instalar_dependencias():
    try:
        # Instalar la biblioteca Tkinter utilizando el gestor de paquetes apt-get
        instalar("Tkinter", "sudo apt-get install python3.tk")

        # Instalar la herramienta Pip utilizando el gestor de paquetes apt
        instalar("Pip", "sudo apt install python3-pip")

        # Comando para instalar las dependencias especificadas en el archivo requirements.txt
        comando = "pip install -r requirements.txt"

        # Ejecutar el comando y mostrar la salida en tiempo real
        with subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, bufsize=1,
                              universal_newlines=True) as proceso:

            # Iterar sobre las líneas de salida del proceso:
            for linea in proceso.stdout:
                # Extraer el nombre de la biblioteca de la línea de salida:
                nombre_biblioteca = linea.strip().split(" ")[1]

                # Si la biblioteca ya se encuentra instalada omitimos el mensaje:
                if nombre_biblioteca != "already":
                    print(f"Instalando la biblioteca: {nombre_biblioteca}")
                else:
                    print(f"Librería ya instalada!")

        # Verificar si la instalación se completó correctamente:
        if proceso.wait() == 0:
            print("¡La instalación de las bibliotecas se ha completado!")
        else:
            print("Se produjo un error durante la instalación de las bibliotecas.")

    except subprocess.CalledProcessError as e:
        print("Error al instalar las dependencias:")
        print(e)

        # Salir del programa con un código de error:
        sys.exit(1)