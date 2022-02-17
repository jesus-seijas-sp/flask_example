from flask import Blueprint, request
from core.http import buildResponse
from controllers import helloworld


main_blueprint = Blueprint("main_blueprint", __name__)


@main_blueprint.route("/hello", methods=["GET"])
def hello():
    return buildResponse(helloworld(request))

