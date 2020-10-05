# Хотел начать сегодня, но с ног валюсь - _ - 01.10.20
# С утреца пару строк осилю :3
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
	return 'Buck me daddy'

@app.route('/The_thing', methods=['GET','POST'])
def The_thing():
	if request.method == 'POST':
		Data_from_POST = request.get_json(force=True)

		filename = "newfile.txt"
		myfile = open(filename, 'w')
		myfile.write(str(Data_from_POST))
		myfile.close()

		return 'Done'

	elif request.method == 'GET':

		filename = "newfile.txt"
		myfile = open(filename, 'r')
		Data_from_POST = myfile.read()
		myfile.close()

		return Data_from_POST

if(__name__) == '__main__':
		app.run(debug = True)
# Пока сиддел разбирался: 
# может написать скрипт для процедурно генерируемой музыки?