import sqlite3


def insert_new_quask(date_created, description, is_done):
	connection = sqlite3.connect('toDO.db')
	cursor = connection.cursor()

	new_quask = [tuple('{0},{1},{2}'.format(date_created, description, is_done).split(','))]
	
	cursor.executemany('INSERT INTO quasks (date_created, description, is_done) VALUES (?,?,?)', new_quask)

	connection.commit()
	connection.close()

	return 'Done\n'
