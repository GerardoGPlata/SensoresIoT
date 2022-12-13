import pymongo
import json
import time

# Conectar Base de datos
cluster = pymongo.MongoClient("mongodb+srv://gerardogplata:$Plata6494@bdnube.frd33vq.mongodb.net/?retryWrites=true&w=majority")

# Crear base de datos
db = cluster["BDNube"]
# Crear coleccion
collection = db["Sensores"]

# Cargar datos a MongoDB
def cargarDatos():
    # Comprobra si el sensor existe en la base de datos
    with open("Sensores.json", "r") as archivo:
        datos = json.load(archivo)
        archivo.close()
    # Comprobar si el sensor existe en la base de datos
    if collection.count_documents({"Nombre": datos["Nombre"]}) == 0:
        collection.insert_one(datos)
    else:
        collection.update_one({"Nombre": datos["Nombre"]}, {"$set": datos})

# Cargar todos los json a MongoDB
def cargarTodos():
    with open("boton.json", "r") as archivo:
        datos = json.load(archivo)
        archivo.close()
    # Comprobar si el sensor existe en la base de datos
    if collection.count_documents({"Nombre": datos["Nombre"]}) == 0:
        collection.insert_one(datos)
    else:
        collection.update_one({"Nombre": datos["Nombre"]}, {"$set": datos})
    with open("banda.json", "r") as archivo:
        datos = json.load(archivo)
        archivo.close()
    # Comprobar si el sensor existe en la base de datos
    if collection.count_documents({"Nombre": datos["Nombre"]}) == 0:
        collection.insert_one(datos)
    else:
        collection.update_one({"Nombre": datos["Nombre"]}, {"$set": datos})
    with open("bomba.json", "r") as archivo:
        datos = json.load(archivo)
        archivo.close()
    # Comprobar si el sensor existe en la base de datos
    if collection.count_documents({"Nombre": datos["Nombre"]}) == 0:
        collection.insert_one(datos)
    else:
        collection.update_one({"Nombre": datos["Nombre"]}, {"$set": datos})
    with open("sensorIR.json", "r") as archivo:
        datos = json.load(archivo)
        archivo.close()
    # Comprobar si el sensor existe en la base de datos
    if collection.count_documents({"Nombre": datos["Nombre"]}) == 0:
        collection.insert_one(datos)
    else:
        collection.update_one({"Nombre": datos["Nombre"]}, {"$set": datos})