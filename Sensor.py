# Importar librerias
import Adafruit_DHT as Adafruit_dht
import time
import json
import board
import RPi.GPIO as GPIO
import os
from MongoDB import cargarTodos


# Sensor detector IR
def sensorIR():
    pin = 22
    # Configurar GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    while True:
        # Comprobar si hay movimiento
        if GPIO.input(pin) == 0:
            # Encender led
            with open("sensorIR.json", "w") as archivo:
                datos = {
                    "Nombre": "Sensor IR",
                    "Estado": 1,
                }
                json.dump(datos, archivo, indent=4)
            archivo.close()
            print("Apagando banda")
            cargarTodos()
            apagarBanda()
            break

def sensorIR2():
    pin = 22
    # Configurar GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    while True:
        if GPIO.input(pin) == 0:
            print("pin: ", GPIO.input(pin))


# Sensor emisor IR
def sensorEmisorIR():
    pin = 23
    # Configurar GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    while True:
        # Encender emisor IR
        GPIO.output(pin, GPIO.HIGH)


# sensor boton
def sensorBoton():
    estatusSensores()
    pin = 17
    # Configurar GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    pararBanda()
    while True:
        # Comprobar si hay movimiento
        if GPIO.input(pin) == 0:
            # Encender led
            estatusSensores()
            with open("boton.json", "w") as archivo:
                datos = {
                    "Nombre": "Boton",
                    "Estado": 1,
                }
                json.dump(datos, archivo, indent=4)
            archivo.close()
            cargarTodos()
            encenderBanda()
            sensorIR()


# Sensor de banda
def encenderBanda():
    print("Encendiendo banda")
    pin = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    # Subir datos a la base de datos
    with open("banda.json", "w") as archivo:
        datos = {
            "Nombre": "Banda",
            "Estado": 1,
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    cargarTodos()


def apagarBanda():
    print("Apagando banda")
    pin = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    # Subir datos a la base de datos
    with open("banda.json", "w") as archivo:
        datos = {
            "Nombre": "Banda",
            "Estado": 0,
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    cargarTodos()
    encenderBomba()
    time.sleep(5)
    encenderBanda()

def pararBanda():
    print("Parando banda")
    pin = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


# enceder bomba de agua
def encenderBomba():
    print("Encendiendo bomba")
    pin = 27
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    # Subir datos a la base de datos
    with open("bomba.json", "w") as archivo:
        datos = {
            "Nombre": "Bomba",
            "Estado": 1,
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    cargarTodos()

# Apagar bomba de agua
def apagarBomba():
    print("Apagando bomba")
    pin = 27
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    # Subir datos a la base de datos
    with open("bomba.json", "w") as archivo:
        datos = {
            "Nombre": "Bomba",
            "Estado": 0,
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    cargarTodos()

def estatusSensores():
    # El estatus de los sensores sera de 0
    with open("sensorIR.json", "w") as archivo:
        datos = {
            "Nombre": "Sensor IR",
            "Estado": 0,
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    with open("boton.json", "w") as archivo:
        datos = {
            "Nombre": "Boton",
            "Estado": 0,
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    with open("banda.json", "w") as archivo:
        datos = {
            "Nombre": "Banda",
            "Estado": 0,
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    with open("bomba.json", "w") as archivo:
        datos = {
            "Nombre": "Bomba",
            "Estado": 0,
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    cargarTodos()