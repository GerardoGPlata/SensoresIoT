import json
import os
import threading
from Sensor import sensorBoton

# Crear json vacio de sensores si no existe
if not os.path.exists("Sensores.json"):
    datos = []
    # Agregar direccion al json sin repetir
    with open("Sensores.json", "w") as file:
        json.dump(datos, file)
    file.close()

# Iniciar Hilo Temperatura y humedad
hilo1 = threading.Thread(target=sensorBoton, args=())
hilo1.start()
