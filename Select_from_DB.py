# БД зачит да?
import sqlite3


def select_last_id():
	connection = sqlite3.connect('toDO.db')
	cursor = connection.cursor()

	cursor.execute('SELECT id FROM quasks ORDER BY id DESC LIMIT 1')
	id_field = int(cursor.fetchone()[0])

	connection.close()

	return id_field


def select_last_quask():
	connection = sqlite3.connect('toDO.db')
	cursor = connection.cursor()
	
	cursor.execute('SELECT * FROM quasks ORDER BY id DESC LIMIT 1')
	last_quask = cursor.fetchone()
	
	connection.close()

	return last_quask


def get_column_names():
	connection = sqlite3.connect('toDO.db')
	cursor = connection.cursor()	
	
	cursor.execute('SELECT id, date_created,  description, is_done FROM quasks')
	names = [description[0] for description in cursor.description]

	return names


def select_all_quasks():
	connection = sqlite3.connect('toDO.db')
	cursor = connection.cursor()

	quasks = cursor.execute('SELECT * FROM quasks ORDER BY id ASC').fetchall()
	
	connection.close()

	return quasks
