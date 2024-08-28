from http import client
from pymongo import MongoClient
import certifi

MONGO_DB_URI = "mongodb+srv://arguelloignaciodev:SYOmBn2Xw0FZBP9K@todoappcluster0.ysd4x.mongodb.net/?retryWrites=true&w=majority&appName=ToDoAppCluster0"

ca = certifi.where()


def dbConnection():
    try:
        client = MongoClient.connect(MONGO_DB_URI, tlsCAPFile=ca)
        db = client("dbb_todo_app")
    except ConnectionError:
        print("Error de conexion")
    return db
