from core.http import buildResponse
from settings import VERSION
from flask import Blueprint

health_blueprint = Blueprint('health_blueprint', __name__)


@health_blueprint.route('/health', methods=['GET'])
def health():
    return buildResponse({"status": "OK", "vesion": VERSION})
