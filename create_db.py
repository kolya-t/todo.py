import sqlite3


def create_db():

	connection = sqlite3.connect('toDO.db')
	cursor = connection.cursor()

	cursor.execute('''CREATE TABLE if not exists quasks 
					('id' INTEGER PRIMARY KEY, 'date_created' integer, 'description' text, 'is_done' integer)''')

	connection.commit()
	connection.close()
	return
