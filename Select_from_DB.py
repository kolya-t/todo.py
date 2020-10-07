# БД зачит да?
import sqlite3
import json

def selection():

	connection = sqlite3.connect('toDO.db')
	cursor = connection.cursor()
	
	cursor.execute('SELECT id FROM quasks ORDER BY id DESC LIMIT 1')

	Id = int(list(cursor.fetchall()[0])[0])
	
	connection.close()

	return Id

def selection_all():

	connection = sqlite3.connect('toDO.db')
	cursor = connection.cursor()
	
	cursor.execute('SELECT * FROM quasks ORDER BY id ASC')
	quasks = cursor.fetchall()
	
	connection.close()

	return quasks