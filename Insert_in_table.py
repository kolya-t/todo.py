# БД зачит да?
import sqlite3
import json

def Insertion(id, date_created, description, is_done):

	connection = sqlite3.connect('toDO.db')
	cursor = connection.cursor()

	new_quask = [tuple('{0},{1},{2},{3}'.format(id, date_created, description, is_done).split(','))]
	print(new_quask)

	cursor.executemany('INSERT INTO quasks VALUES (?,?,?,?)', new_quask)
	connection.commit()
	connection.close()
