# БД зачит да?
import sqlite3
import json

def Selection():

	connection = sqlite3.connect('toDO.db')
	cursor = connection.cursor()
	
	cursor.execute('SELECT id FROM quasks ORDER BY id DESC LIMIT 1')

	Id = int(list(cursor.fetchall()[0])[0])
	print(Id)
	connection.close()

	return Id

def Selection_all():

	connection = sqlite3.connect('toDO.db')
	cursor = connection.cursor()
	
	cursor.execute('SELECT * FROM quasks ORDER BY id ASC')

	quasks = int(list(cursor.fetchall()[0])[0])
	print(quasks)
	connection.close()

	return quasks