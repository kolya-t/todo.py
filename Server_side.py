from flask import Flask, request, jsonify, make_response
from Insert_in_table import insertion
from Request_handling import request_handling_POST
from Select_from_DB import selection, selection_all, last_id
import time

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
	return 'Buck me daddy!'

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
	if request.method == 'POST':

		response = make_response(request_handling_POST())
		response.headers['location'] = 'http://localhost:5000/tasks/' + str(last_id())
		return response

	elif request.method == 'GET':

		tasks_list = selection_all()
		quask_line = ''

		for quask in range(len(tasks_list)):

			quask_line = quask_line + str(tasks_list[quask]) + '\n'
						
		return quask_line	

if(__name__) == '__main__':
		app.run(debug = True)
# curl -X POST 'http://localhost:5000/tasks' -H 'Content-Type: application/json' -d '{"someKey": "some value"}'