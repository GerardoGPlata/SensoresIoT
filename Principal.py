from Sensor import sensorTemperaturaHumedad
from MongoDB import cargarDatos
import threading
import os

# Crear un hilo para ejecutar el sensor de temperatura y humedad
hiloSensor = threading.Thread(target=sensorTemperaturaHumedad, args=())

# Crear un hilo para ejecutar la funcion que inserta los datos en la base de datos
hiloInsertar = threading.Thread(target=cargarDatos, args=())


# Menu para seleccionar que hilo ejecutar
while True:
    # Limpiar consola rapsberry pi
    os.system("clear")
    if hiloSensor.is_alive():
        # Cambiar el color texto a verde
        print("\033[92m")
        print("Sensor de temperatura y humedad ejecutandose")
    if hiloInsertar.is_alive():
        # Cambiar el color texto a verde
        print("\033[92m")
        print("Insertando datos en la base de datos")
    # Cambiar el color texto a blanco
    print("\033[0m")
    print("1. Ejecutar sensor de temperatura y humedad")
    print("2. Insertar datos en la base de datos")
    print("3. Salir")
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        hiloSensor.start()
        print("Ejecutando sensor de temperatura y humedad")
    elif opcion == 2:
        hiloInsertar.start()
        print("Insertando datos en la base de datos")
    elif opcion == 3:
        exit()
    else:
        print("Opcion incorrecta")
