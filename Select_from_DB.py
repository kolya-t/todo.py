# БД зачит да?
import sqlite3
import json

def last_id():

	connection = sqlite3.connect('toDO.db')
	cursor = connection.cursor()
	
	cursor.execute('SELECT id FROM quasks ORDER BY id DESC LIMIT 1')

	Id = int(cursor.fetchone()[0])
		
	connection.close()

	return Id

def selection():

	connection = sqlite3.connect('toDO.db')
	cursor = connection.cursor()
	
	cursor.execute('SELECT * FROM quasks ORDER BY id DESC LIMIT 1')

	last_quask = cursor.fetchone()
	
	connection.close()

	return last_quask

def column_names():

	connection = sqlite3.connect('toDO.db')
	cursor = connection.cursor()	
	
	cursor.execute('SELECT id,  description, date_created, is_done FROM quasks')

	names = [description[0] for description in cursor.description]

	return names 

def selection_all():

	connection = sqlite3.connect('toDO.db')
	cursor = connection.cursor()
	
	cursor.execute('SELECT * FROM quasks ORDER BY id ASC')
	quasks = cursor.fetchall()
	
	connection.close()

	return quasks