from flask import request, make_response
from functools import wraps
from os import environ


def login_user(username, password):
    api_username = environ.get('TODO_USER')
    api_key = environ.get('TODO_PASSWORD')
    return username == api_username and password == api_key


def requires_authorization(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        authorization = request.authorization
        if not (environ.get('TODO_USER') is None or environ.get('TODO_PASSWORD') is None):
            if not authorization:
                return make_response('Authorization is required', 401,
                                     {'WWW-Authenticate': 'Basic realm="Login required"'})
            elif not login_user(authorization.username, authorization.password):
                return make_response('Wrong authorization pare', 403,
                                     {'WWW-Authenticate': 'Basic realm="Login required"'})
            return f(*args, **kwargs)
        return f(*args, **kwargs)
    return decorated
