from crypt import methods
import imp
from flask import Blueprint

#Importacion del Archivo Service
from services.to_do_services import create_to_do_service

#Nombre del Blueprint
to_do = Blueprint("to_do", __name__)

# GET All
@to_do.route("/", methods=["GET"])
def get_to_do_task():
    return "Get all To Do now"

# GET BY ID
@to_do.route("/<id>", methods=["GET"])
def get_to_to_id(id):
    return "Get to do by id"

# POST - (Create)
@to_do.route("/", methods=["POST"])
def post_to_to():
    return create_to_do_service()

# PUT - (Update)
@to_do.route("/<id>", methods=["PUT"])
def update_to_to_id(id):
    return "Update to do by id"

# DELETE BY ID
@to_do.route("/<id>", methods=["DELETE"])
def delete_to_to_id(id):
    return "Delete to do by id"
