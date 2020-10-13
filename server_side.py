from flask import Flask
from request_handling import create_post_response, create_get_response, create_get_id_response, create_patch_id_response
from create_db import create_db

app = Flask(__name__)

create_db()


@app.route('/')
def index():
	return 'Wrong way Bud!', 404


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


if __name__ == '__main__':
	app.run(debug=True)

'''
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
'''
