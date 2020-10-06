# Хотел начать сегодня, но с ног валюсь - _ - 01.10.20
# С утреца пару строк осилю :3
from flask import Flask, request, jsonify
from Insert_in_table import Insertion
import time
from Select_from_DB import Selection, Selection_all


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
	return 'Buck me daddy'

@app.route('/The_thing', methods=['GET','POST'])
def The_thing():
	if request.method == 'POST':
		Data_from_POST = request.get_json()

		date_created = time.time()
		
		Next_Id = int(int(Selection()) + 1)
		
		print(Selection())

		Insertion(Next_Id, date_created, Data_from_POST, 0)

		return 'Done'

	elif request.method == 'GET':

		Selection_all()

		return 'Done'

if(__name__) == '__main__':
		app.run(debug = True)
# Пока сиддел разбирался: 
# может написать скрипт для процедурно генерируемой музыки?