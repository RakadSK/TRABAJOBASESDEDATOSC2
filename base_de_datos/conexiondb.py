from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient
load_dotenv()
contrasena = os.environ.get("MONGO_CONTRASENA")
conexion = f"mongodb+srv://sebastianduque971:{contrasena}@cluster0.boamfkb.mongodb.net/"


def conectar_cliente():
    cliente = None
    try:
        cliente = MongoClient(conexion)
        print("#################")
        print("Conexión exitosa")
        print("/////////////////")
        # dbs = cliente.list_database_names()
        # print(dbs)
    except Exception as e:
        print("||||||||||||||||||||||||||||")
        print("Error de conexión con la BD", e)
        print("||||||||||||||||||||||||||||")

    return cliente
