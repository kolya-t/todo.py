from flask import request, make_response
from decouple import config
from functools import wraps
from os import path


def login_user(username, password):
    api_username = config('TODO_USER')
    api_key = config('TODO_PASSWORD')
    return username == api_username and password == api_key


def requires_authorization(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if path.exists(".env"):
            authorization = request.authorization
            if not authorization:
                return make_response('Authorization is required', 401,
                                     {'WWW-Authenticate': 'Basic realm="Login required"'})
            elif not login_user(authorization.username, authorization.password):
                return make_response('Wrong authorization pare', 403,
                                     {'WWW-Authenticate': 'Basic realm="Login required"'})
            return f(*args, **kwargs)
        return f(*args, **kwargs)
    return decorated
