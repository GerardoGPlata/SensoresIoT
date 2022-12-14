# Importar librerias
import Adafruit_DHT as Adafruit_dht
import time
import json
import board
import RPi.GPIO as GPIO
import os
from MongoDB import cargarTodos

# Sensor ultrasonico para encender
def sensorUltrasonico():
    pinTrig = 24
    pinEcho = 25
    # Configurar GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pinTrig, GPIO.OUT)
    GPIO.setup(pinEcho, GPIO.IN)
    while True:
        # Encender emisor IR
        GPIO.output(pinTrig, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(pinTrig, GPIO.LOW)
        startTime = time.time()
        stopTime = time.time()
        while GPIO.input(pinEcho) == 0:
            startTime = time.time()
        while GPIO.input(pinEcho) == 1:
            stopTime = time.time()
        timeElapsed = stopTime - startTime
        distance = (timeElapsed * 34300) / 2
        #print("Distancia: ", distance, "cm")
        if distance < 10:
            # Apagar banda
            apagarBanda()
            # Encender led
            with open("sensorUltrasonico.json", "w") as archivo:
                datos = {
                    "Nombre": "Sensor Ultrasonico",
                    "Distancia": distance,
                    "Pines": [pinTrig, pinEcho],
                }
                json.dump(datos, archivo, indent=4)
            archivo.close()
            cargarTodos()
            break


# Sensor ultrasonico para apagar
def sensorUltrasonicoApagar():
    pinTrig = 22
    pinEcho = 23
    # Configurar GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pinTrig, GPIO.OUT)
    GPIO.setup(pinEcho, GPIO.IN)
    while True:
        # Encender emisor IR
        GPIO.output(pinTrig, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(pinTrig, GPIO.LOW)
        startTime = time.time()
        stopTime = time.time()
        while GPIO.input(pinEcho) == 0:
            startTime = time.time()
        while GPIO.input(pinEcho) == 1:
            stopTime = time.time()
        timeElapsed = stopTime - startTime
        distance = (timeElapsed * 34300) / 2
        if distance < 10:
            time.sleep(2)
            pararBanda()


# sensor boton
def sensorBoton():
    estatusSensores()
    pararBanda()
    pin = 17
    # Configurar GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    GPIO.setup(4, GPIO.OUT)
    while True:
        # Comprobar si hay movimiento
        if GPIO.input(pin) == 0:
            # Encender led
            GPIO.output(4, GPIO.LOW)
            estatusSensores()
            with open("boton.json", "w") as archivo:
                datos = {
                    "Nombre": "Boton",
                    "Estado": "Encendido",
                    "Pines": [pin],
                }
                json.dump(datos, archivo, indent=4)
            archivo.close()
            cargarTodos()
            # apagar led
            GPIO.output(4, GPIO.HIGH)
            encenderBanda()
            sensorUltrasonico()


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
            "Estado": "Encendida",
            "Pines": [pin],
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
            "Estado": "Apagada",
            "Pines": [pin],
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    cargarTodos()
    encenderBomba()
    time.sleep(5)
    apagarBomba()
    encenderBanda()


def pararBanda():
    pin = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    with open("banda.json", "w") as archivo:
        datos = {
            "Nombre": "Banda",
            "Estado": "Apagada",
            "Pines": [pin],
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    cargarTodos()


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
            "Estado": "Encendida",
            "Pines": [pin],
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
            "Estado": "Apagada",
            "Pines": [pin],
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    cargarTodos()


def estatusSensores():
    # El estatus de los sensores sera de 0
    with open("boton.json", "w") as archivo:
        datos = {
            "Nombre": "Boton",
            "Estado": "Apagado",
            "Pines": 17,
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    with open("banda.json", "w") as archivo:
        datos = {
            "Nombre": "Banda",
            "Estado": "Apagada",
            "Pines": 21,
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    with open("bomba.json", "w") as archivo:
        datos = {
            "Nombre": "Bomba",
            "Estado": "Apagada",
            "Pines": 27,
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    with open("sensorUltrasonico.json", "w") as archivo:
        datos = {
            "Nombre": "Sensor Ultrasonico",
            "Distancia": 0,
            "Pines": [20, 21],
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    cargarTodos()
