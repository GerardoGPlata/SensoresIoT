# Importar librerias
import Adafruit_DHT as Adafruit_dht
import time
import json
import board
import RPi.GPIO as GPIO
import threading
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
    pin = board.D17
    while True:
        # Comprobar si hay movimiento
        if GPIO.input(pin):
            print("Hay movimiento")
        else:
            print("No hay movimiento")
        time.sleep(1)


# Sensor emisor IR
def sensorEmisorIR():
    pin = board.D23
    while True:
        # Encender emisor IR
        GPIO.output(pin, GPIO.HIGH)


# sensor boton
def sensorBoton():
    pin = 17
    # Configurar GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    GPIO.setup(4, GPIO.OUT)
    GPIO.output(4, GPIO.LOW)
    while True:
        # Comprobar si hay movimiento
        if GPIO.input(pin) == 0:
            # Encender led
            GPIO.output(4, GPIO.HIGH)
            with open("Sensores.json", "w") as archivo:
                datos = {
                    "Nombre": "Boton",
                    "Estado": 1,
                }
                json.dump(datos, archivo, indent=4)
            archivo.close()
            # Iniciar hilo de temperatura y humedad
            hilo1 = threading.Thread(target=sensorTemperaturaHumedad, args=())
            hilo1.start()
            break
        else:
            time.sleep(1)
