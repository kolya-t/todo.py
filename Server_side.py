from flask import Flask, request, jsonify
from Insert_in_table import insertion
import time
from Select_from_DB import selection, selection_all

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
	return 'Buck me daddy!'

@app.route('/The_thing', methods=['GET', 'POST'])
def the_thing():
	if request.method == 'POST':

		Data_from_POST = request.get_json()
		date_created = int(time.time() * 1000)

		insertion(date_created, Data_from_POST, 0)
		return 'Done\n'

	elif request.method == 'GET':

		The_things_list = selection_all()
		quask_line = ''

		for quask in range(len(The_things_list)):

			quask_line = quask_line + str(The_things_list[quask]) + '\n'
						
		return quask_line	

if(__name__) == '__main__':
		app.run(debug = True)
# curl -X POST 'http://localhost:5000/The_thing' -H 'Content-Type: application/json' -d '{"someKey": "some value"}'