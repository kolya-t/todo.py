import sqlite3


def update_is_done_quask(is_done_value, quask_num):
	connection = sqlite3.connect('toDO.db')
	cursor = connection.cursor()

	quask_data_list = [(str(is_done_value), str(quask_num))]

	cursor.executemany('UPDATE quasks SET is_done = (?) WHERE id = (?)', quask_data_list)

	connection.commit()
	connection.close()

	return 'Done\n'
