from core.http import buildResponse, HttpException
from flask import Blueprint

error_blueprint = Blueprint('error_blueprint', __name__)


@error_blueprint.app_errorhandler(HttpException)
def handle_exception(e):
    response = buildResponse(e)
    return response
