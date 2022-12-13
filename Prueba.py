import json
import os
import threading
from Sensor import sensorBoton, sensorIR, sensorEmisorIR

# Crear json vacio de sensores si no existe
if not os.path.exists("Sensores.json"):
    datos = []
    # Agregar direccion al json sin repetir
    with open("Sensores.json", "w") as file:
        json.dump(datos, file)
    file.close()

# Iniciar Hilo Temperatura y humedad
hiloBoton = threading.Thread(target=sensorBoton, args=())
hiloSensorIR = threading.Thread(target=sensorIR, args=())
hiloSensorEmisorIR = threading.Thread(target=sensorEmisorIR, args=())

hiloBoton.start()
hiloSensorEmisorIR.start()
hiloSensorIR.start()
