# Хотел начать сегодня, но с ног валюсь - _ - 01.10.20
# С утреца пару строк осилю :3
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
	return "Suck me daddy"