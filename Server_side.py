from flask import Flask  # , request
from Request_handling import create_post_response, create_get_response
from Create_DB import  create_db

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


if __name__ == '__main__':
	app.run(debug=True)

'''
forUnix
curl -X POST 'http://localhost:5000/tasks' -H 'Content-Type: application/json' -d '{"description": "some value"}'
forWin 
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d "{\"description\":\"some value\"}"
'''
