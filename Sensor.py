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
        # print("Distancia: ", distance, "cm")
        if distance < 10:
            # Apagar banda
            apagarBanda()
            # Encender led
            with open("sensorUltrasonico.json", "w") as archivo:
                datos = {
                    "Nombre": "Sensor Ultrasonico",
                    "Estado": "Encendido",
                    "Distancia": distance,
                    "Pines": [pinTrig, pinEcho],
                    "Fecha": time.strftime("%d/%m/%y/%H:%M:%S"),
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
            # Mandar datos a la base de datos
            with open("sensorUltrasonicoApagar.json", "w") as archivo:
                datos = {
                    "Nombre": "Sensor Ultrasonico",
                    "Estado": "Apagado",
                    "Distancia": distance,
                    "Pines": [pinTrig, pinEcho],
                    "Fecha": time.strftime("%d/%m/%y/%H:%M:%S"),
                }
                json.dump(datos, archivo, indent=4)
            pararBanda()


# sensor boton
def sensorBoton():
    estatusSensores()
    pararBanda()
    pin = 17
    # Configurar GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    GPIO.setup(27, GPIO.OUT)
    GPIO.output(27, GPIO.LOW)
    while True:
        # Comprobar si hay movimiento
        if GPIO.input(pin) == 0:
            # Encender led
            estatusSensores()
            with open("boton.json", "w") as archivo:
                datos = {
                    "Nombre": "Boton",
                    "Estado": "Encendido",
                    "Pines": [pin],
                    "Fecha": time.strftime("%d/%m/%y/%H:%M:%S"),
                }
                json.dump(datos, archivo, indent=4)
            archivo.close()
            cargarTodos()
            encenderBanda()
            sensorUltrasonico()


# Sensor de banda
def encenderBanda():
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
            "Fecha": time.strftime("%d/%m/%y/%H:%M:%S"),
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    cargarTodos()


def apagarBanda():
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
            "Fecha": time.strftime("%d/%m/%y/%H:%M:%S"),
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    cargarTodos()
    encenderBomba()
    time.sleep(5)
    apagarBomba()
    encenderBanda()
    cargarTodos()


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
            "Fecha": time.strftime("%d/%m/%y/%H:%M:%S"),
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    cargarTodos()


# enceder bomba de agua
def encenderBomba():
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
            "Fecha": time.strftime("%d/%m/%y/%H:%M:%S"),
            "Litros": 0,
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    cargarTodos()


# Apagar bomba de agua
def apagarBomba():
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
            "Fecha": time.strftime("%d/%m/%y/%H:%M:%S"),
            "Litros": 0,
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
            "Pines": [17],
            "Fecha": time.strftime("%d/%m/%y/%H:%M:%S"),
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    with open("banda.json", "w") as archivo:
        datos = {
            "Nombre": "Banda",
            "Estado": "Apagada",
            "Pines": [21],
            "Fecha": time.strftime("%d/%m/%y/%H:%M:%S"),
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    with open("bomba.json", "w") as archivo:
        datos = {
            "Nombre": "Bomba",
            "Estado": "Apagada",
            "Pines": [27],
            "Fecha": time.strftime("%d/%m/%y/%H:%M:%S"),
            "Litros": 0,
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    with open("sensorUltrasonico.json", "w") as archivo:
        datos = {
            "Nombre": "Sensor Ultrasonico",
            "Estado": "Apagado",
            "Distancia": 0,
            "Pines": [20, 21],
            "Fecha": time.strftime("%d/%m/%y/%H:%M:%S"),
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    cargarTodos()


# Sensor Flujo de agua
def sensorFlujo():
    pin = 13
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN)
    rate_cnt = 0
    tot_cnt = 0
    minutes = 0
    constant = 0.10
    time_new = 0.0
    time_new = time.time() + 10
    rate_cnt = 0
    while time.time() <= time_new:
        if GPIO.input(input) != 0:
            rate_cnt += 1
            tot_cnt += 1
    minutes += 1
    # Enviar Datos a la base de datos
    with open("bomba.json", "w") as archivo:
        datos = {
            "Nombre": "Bomba de Agua",
            "Estado": "Encendido",
            "Pines": [13],
            "Fecha": time.strftime("%d/%m/%y/%H:%M:%S"),
            "Litros": round(tot_cnt * constant, 4),
        }
        json.dump(datos, archivo, indent=4)
    archivo.close()
    cargarTodos()
