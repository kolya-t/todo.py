from flask import Flask, request, make_response
from request_handling import create_post_response, create_get_response, create_get_id_response, create_patch_id_response
from create_db import create_db
from decouple import config
from functools import wraps


def login_user(username, password):
	api_username = config('TODO_USER')
	api_key = config('TODO_PASSWORD')
	return username == api_username and password == api_key


def requires_authorization(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		authorization = request.authorization
		if not authorization:
			return make_response('Nah', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})
		elif not login_user(authorization.username, authorization.password):
			return make_response('Nope', 403, {'WWW-Authenticate': 'Basic realm="Login required"'})

		return f(*args, **kwargs)
	return decorated


app = Flask(__name__)

create_db()


@app.route('/')
@requires_authorization
def index():
	return 'Wrong way Bud!'


@app.route('/tasks', methods=['POST'])
def responding_to_post():
	return create_post_response()


@app.route('/tasks', methods=['GET'])
def respond_to_get():
	return create_get_response()


@app.route('/tasks/<int:quask_num>', methods=['GET'])
def respond_to_get_id(quask_num):
	return create_get_id_response(quask_num)


@app.route('/tasks/<int:quask_num>', methods=['PATCH'])
def respond_to_patch_id(quask_num):
	return create_patch_id_response(quask_num)


'''
@app.route('/account/login')
def login_user():
	API_USERNAME = config('TODO_USER')
	API_KEY = config('TODO_PASSWORD')
	if request.authorization and request.authorization.username == API_USERNAME \
		and request.authorization.password == API_KEY:
		return make_response("Logged", 200)
	else:
		return make_response('Nope', 403,{'WWW-Authenticate': 'Basic realm="Login required"'})
	# return make_response('Not Authenticate yet', 401,{'WWW-Authenticate': 'Basic realm="Login required"'})




if __name__ == '__main__':
	app.run(debug=True)


POSTforUnix
curl -X POST 'http://localhost:5000/tasks' -H 'Content-Type: application/json' -d '{"description": "some value"}'
POSTforWin 
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d "{\"description\":\"some value\"}"
GET_IDforWin
-X GET http://localhost:5000/tasks/62 -i
GETforWin
-X GET http://localhost:5000/tasks
PATCHforWin
-X PATCH http://localhost:5000/tasks/1 -i -H "Content-Type: application/json" -d "{\"is_done\":\"1\"}"
LOGINforWIN
curl -u Sanya:Kolya http://localhost:5000/account/login
'''
