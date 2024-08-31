from unittest import result
from flask import request
from config.mongodb import mongo


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
