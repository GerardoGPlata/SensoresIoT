import json
import os
import threading
import RPi.GPIO as GPIO
from Sensor import sensorBoton, estatusSensores, sensorUltrasonicoApagar
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
apagarBanda()
cargarTodos()

# Iniciar Hilo Temperatura y humedad
hiloBoton = threading.Thread(target=sensorBoton, args=())
hiloUltrasonico = threading.Thread(target=sensorUltrasonicoApagar, args=())
hiloBoton.start()
hiloUltrasonico.start()