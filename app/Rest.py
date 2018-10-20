from flask import Blueprint
from app import app

rest_api = Blueprint('rest_api', __name__)

@rest_api.route("/")
def helloRest():
    return "Hello Rest"
