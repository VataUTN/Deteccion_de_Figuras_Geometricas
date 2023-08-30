# Geometric Shapes Detection Project

## Team Profiles

| Name            | Role            | Avatar                                 |
|-----------------|-----------------|----------------------------------------|
| Luca Zamperoni  | Product Owner   | <img src="https://avatars.githubusercontent.com/u/129890529?v=4" width="100px" height="100px">  |
| Valentin Tamola | Developer       | <img src="https://avatars.githubusercontent.com/u/129886045?v=4" width="100px">  |
| Jazmín Rillo    | Developer       | <img src="https://avatars.githubusercontent.com/u/129994394?s=70&v=4" width="100px">  |
| Franco Santibañez | Developer      | <img src="https://avatars.githubusercontent.com/u/129998263?s=70&v=4" width="100px">  |
| Lucas Cardone   | Developer       | <img src="https://avatars.githubusercontent.com/u/129989551?v=4" width="100px">  |

---

The objective of this project is to implement an **artificial neural network for the recognition of geometric shapes**, teaching the computer to process a dataset with different images of various shapes. Currently, the network is trained with images of **circles**, **squares**, and **triangles**, which means the network has three possible outputs.

The idea is to develop a user interface that allows the user to input an image containing a geometric shape, and the program will display the result on the same interface, for example, with the text "Square," followed by the **confidence percentages** for each shape obtained by the network.

Internally, the program will have a **dataset** containing training and validation images. This dataset will be used to teach the computer through a trainer that will have a convolutional model within it. This model includes different layers of neurons, batch size, input and output format, among other functionalities that have been added throughout the project's development.

## Installation on Linux
To install and run the project, follow these steps:

Requirements: [requirements.txt](https://github.com/Grupo-E-Metodologia-de-la-Investigacion/Proyecto_MI/blob/main/Codigo/requirements.txt)

1. Make sure you have **Python** installed on your system. You can check by using the following command:

```
python --version
```

With the above command, you should be able to see the installed Python version on your system. If you have multiple Python versions, you can use the same command with "python3."

2. **OPTIONAL** (pip might be automatically installed later): Ensure you have **pip** installed on your system. In some cases, installing pip can lead to issues due to various existing versions. If you encounter problems, you can try running the following commands in order:

```
sudo apt update
sudo apt install curl
wget https://bootstrap.pypa.io/get-pip.py
sudo apt install python3-pip
pip install pip==22.3.1 --break-system-packages
```

Note: If you don't have it installed, it will be automatically installed when you run the program later.

3. Install git to clone the project:

```
sudo apt install git
```

4. Clone the repository to your local machine:
   
```
git clone https://github.com/Grupo-E-Metodologia-de-la-Investigacion/Proyecto_MI.git
```

5. Download and install the **necessary libraries**. You can do this in two ways:

a. Option 1 (Recommended): Automatic requirements download:
   - Follow the steps specified in "Usage," and the requirements will be automatically downloaded if you don't have them installed on your system (this step may take some time and require some confirmations).
   - If for some reason this option doesn't work, you can try manually downloading the required libraries.

b. Option 2: Manually install the requirements:
   - Open a terminal in the project directory.
   - Run the following commands to install the requirements:

     ```
     sudo apt install python3-tk
     sudo apt install python3-pil.imagetk
     sudo apt install python3-numpy
     pip install tensorflow
     ```
     
In both cases, make sure you have an active internet connection.

6. Once you have completed the above steps, you are ready to run the project and use the geometric shapes detection.

---

## Usage
Go to the project directory:

```
cd Proyecto_MI/Codigo
```

To start the program, execute the following command:

```
sudo python3 main.py
```

Once you run the code, the dependencies will be downloaded automatically, and you will see the following application interface:

![First Flow](https://cdn.discordapp.com/attachments/1081778303406448753/1109972318224130138/image.png)

To load an image and perform geometric shapes detection with the neural network, simply click the **"Cargar imagen"** button. This will open a dialog that allows you to select a file from your computer. We have provided some test images in this repository for you to try out! The neural network will then process the image and display the detection results, as illustrated in the following image:

![Second Flow](https://cdn.discordapp.com/attachments/1081778303406448753/1109971690080968855/image.png)

_In the latest version of the project, confidence percentages are added to this result._

We invite you to explore and experiment with different images to see how the neural network detects and classifies geometric shapes in real-time. Remember that the network only recognizes circles, squares, and triangles.

Thank you for your interest and contribution to this exciting geometric shapes detection project!

## Contribution
Thank you for your interest in contributing to the project. Currently, we are not accepting contributions.

## License
None

---

Thank you for reviewing our geometric shapes detection project!
