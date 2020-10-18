from flask import Flask
import logging
from request_handling import create_post_response, create_get_response, create_get_id_response, create_patch_id_response
from create_db import create_db
from authorization import requires_authorization

logging.basicConfig(filename='complete.log', level=logging.DEBUG)
create_db()
app = Flask(__name__)


@app.route('/')
@requires_authorization
def index():
	return 'Wrong way Bud!'


@app.route('/tasks', methods=['POST'])
@requires_authorization
def responding_to_post():
	return create_post_response()


@app.route('/tasks', methods=['GET'])
@requires_authorization
def respond_to_get():
	return create_get_response()


@app.route('/tasks/<int:quask_num>', methods=['GET'])
@requires_authorization
def respond_to_get_id(quask_num):
	return create_get_id_response(quask_num)


@app.route('/tasks/<int:quask_num>', methods=['PATCH'])
@requires_authorization
def respond_to_patch_id(quask_num):
	return create_patch_id_response(quask_num)


if __name__ == '__main__':
	app.run(debug=True)

'''
POST for Unix
curl -X POST 'http://localhost:5000/tasks' -H 'Content-Type: application/json' -d '{"description": "some value"}'

POST for Win
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d "{\"description\":\"some value\"}"

GET_ID for Win
curl -X GET http://localhost:5000/tasks/62 -i

GET for Win
curl -X GET http://localhost:5000/tasks

PATCH for Win
curl -X PATCH http://localhost:5000/tasks/1 -i -H "Content-Type: application/json" -d "{\"is_done\":\"1\"}"

LOGIN for WIN
curl -u admin:admin http://localhost:5000/

Env vars
set FLASK_APP=server_side.py
set TODO_USER=admin
set TODO_PASSWORD=admin

'''
