from io import BytesIO
import json
from flask import Response, send_file


class HttpException(Exception):
    def __init__(self, message, status=500):
        super().__init__(message)
        self.message = message
        self.status = status


class HttpResponse:
    def __init__(self, message, status=200):
        self.message = message
        self.status = status


class HttpFile:
    def __init__(self, file, mimetype):
        if isinstance(file, bytes):
            self.file = BytesIO(file)
        else:
            self.file = file
        self.mimetype = mimetype


def buildResponse(message, status=200):
    if isinstance(message, HttpResponse) or isinstance(message, HttpException):
        return buildResponse(message.message, message.status)
    if isinstance(message, HttpFile):
        return send_file(message.file, message.mimetype)
    if type(message) is dict or isinstance(message, list):
        return Response(response=json.dumps(message), status=status, mimetype="application/json")
    return Response(response=message, status=status)
