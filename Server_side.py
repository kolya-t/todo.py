from flask import Flask, request
from Request_handling import getting_post_request, getting_get_request

app = Flask(__name__)


@app.route('/')
def index():
	return 'Wrong way Bud!', 404


@app.route('/tasks', methods=['GET', 'POST'])
def getting_a_request():
	if request.method == 'POST':
		return getting_post_request()
	elif request.method == 'GET':
		return getting_get_request()


if __name__ == '__main__':
	app.run(debug=True)

'''
forUnix
curl -X POST 'http://localhost:5000/tasks' -H 'Content-Type: application/json' -d '{"description": "some value"}'
forWin 
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d "{\"description\":\"some value\"}"
'''
