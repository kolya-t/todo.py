from flask import Flask  # , request
from request_handling import create_post_response, create_get_response, create_get_id_response
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
	quask_num = quask_num
	return create_get_id_response(quask_num)


if __name__ == '__main__':
	app.run(debug=True)

'''
forUnix
curl -X POST 'http://localhost:5000/tasks' -H 'Content-Type: application/json' -d '{"description": "some value"}'
forWin 
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d "{\"description\":\"some value\"}"
'''
