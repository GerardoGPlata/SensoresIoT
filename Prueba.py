import json
import os
import threading
import RPi.GPIO as GPIO
from Sensor import sensorBoton, estatusSensores
from MongoDB import cargarTodos

# Conectar pines
# sensorBoton pin 17
# sensorIR pin 22
# sensorEmisorIR pin 23
# sensorBanda pin 21
# sensorBomba pin 27

# Apagar banda
def apagarBanda():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)
    GPIO.output(21, GPIO.LOW)


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
if not os.path.exists("sensorIR.json"):
    datos = []
    # Agregar direccion al json sin repetir
    with open("sensorIR.json", "w") as file:
        json.dump(datos, file)
    file.close()

# Inicio con la banda apagada
estatusSensores()
apagarBanda()
cargarTodos()

# Iniciar Hilo Temperatura y humedad
hiloBoton = threading.Thread(target=sensorBoton, args=())
hiloBoton.start()
