# Importar librerias
import Adafruit_DHT as Adafruit_dht
import time
import json
import board
import RPi.GPIO as GPIO
import os
from MongoDB import cargarDatos

# Sensor Temperatura y humedad DHT11
def sensorTemperaturaHumedad():
    # Configurar GPIO
    GPIO.setup(4, GPIO.OUT)
    GPIO.output(4, GPIO.LOW)
    sensor = Adafruit_dht.DHT11
    pin = 24
    while True:
        os.system("clear")
        humedad, temperatura = Adafruit_dht.read(sensor, pin)
        if humedad is not None and temperatura is not None:
            GPIO.output(4, GPIO.HIGH)
            with open("Sensores.json", "w") as archivo:
                datos = {
                    "Nombre": "DHT11",
                    "Temperatura": temperatura,
                    "Humedad": humedad,
                }
                print("Temperatura: ", temperatura)
                print("Humedad: ", humedad)
                json.dump(datos, archivo, indent=4)
            archivo.close()
            cargarDatos()
        time.sleep(3)
        GPIO.output(4, GPIO.LOW)


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
            with open("Sensores.json", "w") as archivo:
                datos = {
                    "Nombre": "IR",
                    "Estado": 0,
                }
                json.dump(datos, archivo, indent=4)
            archivo.close()
            apagarBanda()
            break


# Sensor emisor IR
def sensorEmisorIR():
    pin = 23
    # Configurar GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    while True:
        # Comprobar si hay movimiento
        if GPIO.input(pin) == 0:
            # Encender led
            with open("Sensores.json", "w") as archivo:
                datos = {
                    "Nombre": "IR",
                    "Estado": 1,
                }
                json.dump(datos, archivo, indent=4)
            archivo.close()
            apagarBanda()
            break


# sensor boton
def sensorBoton():
    pin = 17
    # Configurar GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    GPIO.setup(21, GPIO.OUT)
    GPIO.output(21, GPIO.LOW)
    while True:
        # Comprobar si hay movimiento
        if GPIO.input(pin) == 0:
            # Encender led
            with open("Sensores.json", "w") as archivo:
                datos = {
                    "Nombre": "Boton",
                    "Estado": 1,
                }
                json.dump(datos, archivo, indent=4)
            archivo.close()
            encenderBanda()
            break


# Sensor de banda
def encenderBanda():
    pin = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)


def apagarBanda():
    pin = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    sensorBomba()
    time.sleep(3)
    encenderBanda()


# enceder bomba de agua
def sensorBomba():
    pin = 27
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(pin, GPIO.LOW)
    encenderBanda()
