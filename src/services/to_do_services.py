# Importaciones
from flask import request, Response
from config.mongodb import mongo
from bson import json_util, ObjectId


# ? Service para crear tareas - (POST)
def create_to_do_service():
    data = request.get_json()
    name = data.get("name", None)
    date = data.get("date", None)
    type = data.get("type", None)
    if name and date and type:
        response = mongo.db.todos.insert_one(
            {"name": name, "date": date, "type": type, "done": False}
        )
        result = {
            "id": str(response.inserted_id),
            "name": name,
            "date": date,
            "type": type,
            "done": False,
        }
        return result
    else:
        return "Invalid Payload", 400


# ? Service para obtener todos los datos - (GET)
def get_all_to_do_service():
    data = mongo.db.todos.find()
    result = json_util.dumps(data)
    return Response(result, mimetype="application/json")


# ? Service para obtener dato por ID - (GET <ID>)
def get_to_do_for_id_service(id):
    data = mongo.db.todos.find_one({"_id": ObjectId(id)})
    result = json_util.dumps(data)
    return Response(result, mimetype="application/json")


# ? Service para modificar dato - (Update)
def update_to_do_service(id):
    data = request.get_json()
    if len(data) == 0:
        return "Invalid Payload", 400
    response = mongo.db.todos.update_one({"_id": ObjectId(id)}, {"$set": data})
    if response.modified_count >= 1:
        return "Todo updated succesfully", 200
    else:
        return "Todo not found", 404


# ? Service para eliminar dato - (Delete)
def delete_to_do_service(id):
    response = mongo.db.todos.delete_one({"_id": ObjectId(id)})
    if response.deleted_count >= 1:
        return "Todo deleted succesfully", 200
    else:
        return "Todo not found", 404
