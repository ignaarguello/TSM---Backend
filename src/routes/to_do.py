from crypt import methods
import imp
from flask import Blueprint

# Importacion del Archivo Service
from services.to_do_services import (
    create_to_do_service,
    get_all_to_do_service,
    get_to_do_for_id_service,
    update_to_do_service,
    delete_to_do_service,
)

# Nombre del Blueprint
to_do = Blueprint("to_do", __name__)


# GET All
@to_do.route("/", methods=["GET"])
def get_to_do_task():
    return get_all_to_do_service()


# GET BY ID
@to_do.route("/<id>", methods=["GET"])
def get_to_to_id(id):
    return get_to_do_for_id_service(id)


# POST - (Create)
@to_do.route("/", methods=["POST"])
def post_to_to():
    return create_to_do_service()


# PUT - (Update)
@to_do.route("/<id>", methods=["PUT"])
def update_to_to_id(id):
    return update_to_do_service(id)


# DELETE BY ID
@to_do.route("/<id>", methods=["DELETE"])
def delete_to_to_id(id):
    return delete_to_do_service(id)
