# Proyecto de Detección de Figuras Geométricas

![Título del Proyecto](https://cdn.discordapp.com/attachments/1081778303406448753/1109979459093794846/image.png)

## Perfiles de los Integrantes

| Nombre            | Rol                | Avatar                                  |
|-------------------|--------------------|-----------------------------------------|
| Luca Zamperoni    | Product Owner      | <img src="https://avatars.githubusercontent.com/u/129890529?v=4" width="100px" height="100px">  |
| Valentin Tamola   | Developer          | <img src="https://avatars.githubusercontent.com/u/129886045?v=4" width="100px">  |
| Jazmín Rillo      | Developer          | <img src="https://avatars.githubusercontent.com/u/129994394?s=70&v=4" width="100px">  |
| Franco Santibañez | Developer          | <img src="https://avatars.githubusercontent.com/u/129998263?s=70&v=4" width="100px">  |
| Lucas Cardone     | Developer          | <img src="https://avatars.githubusercontent.com/u/129989551?v=4" width="100px">  |

---

El objetivo del proyecto es implementar una red neuronal artificial para el reconocimiento de figuras geométricas, enseñándole a la computadora a procesar un set de datos ingresados con distintas imágenes de diferentes figuras. Actualmente la red está entrenada con imágenes de círculos, cuadrados y triángulos, esto quiere decir que la red tiene tres posibles salidas.
La idea es desarrollar una interfaz de usuario que permita al usuario ingresar una imagen que contenga una figura geométrica y el programa le mostrará sobre esa misma interfaz el resultado, por ejemplo con el texto: “Cuadrado”. 
Internamente, el programa poseerá un set de datos que contendrá las imágenes de entrenamiento y de validación. Este set de datos servirá para enseñarle a la computadora a través de un entrenador que tendrá dentro de sí un modelo convolucional. Este modelo cuenta con las diferentes capas de neuronas, el tamaño del bache y el formato de entrada y salida, entre otras funcionalidades que se fueron agregando a lo largo del desarrollo del proyecto.


## Instalación
Para instalar y ejecutar el proyecto, sigue los siguientes pasos:

Requisitos: [requirements.txt](https://github.com/Grupo-E-Metodologia-de-la-Investigacion/Proyecto_MI/blob/main/Codigo/requirements.txt)

1. Asegúrate de tener instalado Python en tu sistema. Para verificar puedes utilizar el siguiente comando:
```
python --version
```
Con el comando anterior deberías poder ver la versión de Python instalada en tu sistema. Si tienes múltiples versiones de Python puedes usar el comando anterior reemplazando "python" por "python3".

2. Asegúrate de tener instalado pip en tu sistema. En algunas versiones esta instalación puede acarrear algunos problemas relacionados a las distintas versiones existentes. En caso de tener problemas puede intentar ejecutando los siguientes comandos en orden:
```
sudo apt update
sudo apt install curl
wget https://bootstrap.pypa.io/get-pip.py
sudo apt install python3-pip
pip install pip==22.3.1 --break-system-packages
```

3. Instalar git para poder clonar el proyecto:
```
sudo apt install git
```
4. Clona el repositorio en tu máquina local:
```
git clone https://github.com/Grupo-E-Metodologia-de-la-Investigacion/Proyecto_MI.git
```
5. Descarga e instala las librerías necesarias. Puedes hacerlo de dos maneras:

a. Opción 1: Manualmente instalando los requisitos:

   - Abre una terminal en el directorio del proyecto.
   - Ejecuta los siguientes comandos para instalar los requisitos:
 
     ```
     sudo apt install python3-tk
     sudo apt install python3-pil.imagetk
     sudo apt install python3-numpy
     sudo apt install python3-opencv
     pip install tensorflow
     ```
b. Opción 2: Descarga automática de requisitos:

   - Una vez ejecutes el proyecto, los requisitos se descargarán automáticamente si no los tienes instalados en tu sistema.

En ambos casos, asegúrate de tener una conexión a internet activa.

6. Una vez completados los pasos anteriores, estás listo para ejecutar el proyecto y utilizar la detección de figuras geométricas.

---

## Uso
Ve al directorio del proyecto:
```
cd Proyecto_MI/Codigo
```
Para iniciar el programa debe ejecutar el siguiente comando:
```
sudo python3 main.py
```
Una vez ejecutes el código, las dependencias se descargarán automáticamente (este paso puede demorar algunos minutos dependiendo de tu conexión a internet) y se mostrará la siguiente interfaz de la aplicación:

![Primer Flujo](https://cdn.discordapp.com/attachments/1081778303406448753/1109972318224130138/image.png)

Para cargar una imagen y realizar la detección de figuras geométricas con la red neuronal, simplemente selecciona el botón "Cargar imagen". Esto abrirá un diálogo que te permitirá seleccionar un archivo de tu ordenador. A continuación, la red neuronal procesará la imagen y mostrará los resultados de detección, como se ilustra en la siguiente imagen (es posible que la ejecución demore un poco):

![Segundo Flujo](https://cdn.discordapp.com/attachments/1081778303406448753/1109971690080968855/image.png)

Te invitamos a explorar y experimentar con diferentes imágenes para observar cómo la red neuronal detecta y clasifica las formas geométricas en tiempo real. Recuerda que la red sólo reconoce círculos, cuadrados y triángulos. Si el porcentaje de reconocimiento es menor al requerido para considerarse como una de las tres figuras, la interfaz mostrará un mensaje diciendo "No se ha reconocido ninguna figura" y mostrará en pantalla los porcentajes de cada figura.
¡Gracias por tu interés y contribución en este emocionante proyecto de detección de figuras geométricas!

## Contribución

Gracias por interesarte en contribuir al proyecto. Actualmente no estamos recibiendo contribuciones en el mismo.

## Licencia

Ninguna

---

¡Gracias por revisar nuestro proyecto de detección de figuras geométricas!
