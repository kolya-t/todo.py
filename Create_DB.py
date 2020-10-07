# БД зачит да?
import sqlite3

def creation_of_DB():

	connection = sqlite3.connect('toDO.db')
	cursor = connection.cursor()

	cursor.execute('''CREATE TABLE quasks
	             ('id' INTEGER PRIMARY KEY, 'date_created' integer, 'description' text, 'is_done' integer)''')

	connection.commit()
	connection.close()
	return