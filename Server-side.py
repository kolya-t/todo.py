# Хотел начать сегодня, но с ног валюсь - _ - 01.10.20
# С утреца пару строк осилю :3
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
	return 'Home page'

@app.route('/The thing', methods=['POST'])
def The_thing():
	if request.method == 'POST':
		return 'Suck me daddy'
