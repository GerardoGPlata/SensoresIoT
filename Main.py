import json
import os
import threading
import RPi.GPIO as GPIO
import time
from Sensor import sensorBoton, estatusSensores, sensorUltrasonicoApagar, pararBanda
from MongoDB import cargarTodos

# Conectar pines
# sensorBoton pin 17
# sensorIR pin 22
# sensorEmisorIR pin 23
# sensorBanda pin 21
# sensorBomba pin 27


# Crear json vacio de sensores si no existe
if not os.path.exists("boton.json"):
    datos = []
    # Agregar direccion al json sin repetir
    with open("boton.json", "w") as file:
        json.dump(datos, file)
    file.close()
if not os.path.exists("banda.json"):
    datos = []
    # Agregar direccion al json sin repetir
    with open("banda.json", "w") as file:
        json.dump(datos, file)
    file.close()
if not os.path.exists("bomba.json"):
    datos = []
    # Agregar direccion al json sin repetir
    with open("bomba.json", "w") as file:
        json.dump(datos, file)
    file.close()
if not os.path.exists("sensorUltrasonico.json"):
    datos = []
    # Agregar direccion al json sin repetir
    with open("sensorUltrasonico.json", "w") as file:
        json.dump(datos, file)
    file.close()

# Inicio con la banda apagada
estatusSensores()
# pararBanda()
cargarTodos()

# Iniciar Hilo Temperatura y humedad
hiloBoton = threading.Thread(target=sensorBoton, args=())
hiloUltrasonico = threading.Thread(target=sensorUltrasonicoApagar, args=())
hiloBoton.start()
hiloUltrasonico.start()

# Mostrar datos de sensores en la pantalla
while True:
    os.system("clear")
    print("Presione Ctrl + C para salir")
    print("Boton: ", end="")
    with open("boton.json", "r") as file:
        datos = json.load(file)
    file.close()
    # Escribir el estado en color verde si esta encendido
    if datos["Estado"] == "Encendido":
        print("\033[92m", end="")
        print(datos["Estado"])
        print("\033[0m", end="")
    else:
        print("\033[91m", end="")
        print(datos["Estado"])
        print("\033[0m", end="")
    print("Banda: ", end="")
    with open("banda.json", "r") as file:
        datos = json.load(file)
    file.close()
    # Escribir el estado en color verde si esta encendido
    if datos["Estado"] == "Encendida":
        print("\033[92m", end="")
        print(datos["Estado"])
        print("\033[0m", end="")
    else:
        print("\033[91m", end="")
        print(datos["Estado"])
        print("\033[0m", end="")
    print("Bomba: ", end="")
    with open("bomba.json", "r") as file:
        datos = json.load(file)
    file.close()
    # Escribir el estado en color verde si esta encendido
    if datos["Estado"] == "Encendida":
        print("\033[92m", end="")
        print(datos["Estado"])
        print("\033[0m", end="")
    else:
        print("\033[91m", end="")
        print(datos["Estado"])
        print("\033[0m", end="")
    print("Sensor Ultrasonico: ", end="")
    with open("sensorUltrasonico.json", "r") as file:
        datos = json.load(file)
    file.close()
    # Escribir el estado en color verde si esta encendido
    if datos["Estado"] == "Encendido":
        print("\033[92m", end="")
        print(datos["Estado"])
        print("\033[0m", end="")
    else:
        print("\033[91m", end="")
        print(datos["Estado"])
        print("\033[0m", end="")
    time.sleep(1)
