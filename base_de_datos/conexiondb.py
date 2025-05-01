from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient
import certifi
load_dotenv()
user = os.environ.get("MONGO_USER")
contrasena = os.environ.get("MONGO_CONTRASENA")
conexion = f"mongodb+srv://{user}:{contrasena}@cluster0.boamfkb.mongodb.net/"


def conectar_cliente():
    cliente = None
    try:
        cliente = MongoClient(conexion, tls=True, tlsCAFile=certifi.where())
        print(conexion)
        print("Conexión exitosa")
        # dbs = cliente.list_database_names()
        # print(dbs)
    except Exception as e:
        print("||||||||||||||||||||||||||||")
        print("Error de conexión con la BD", e)
        print("||||||||||||||||||||||||||||")

    return cliente
