# БД зачит да?
import sqlite3

connection = sqlite3.connect('toDO.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE quasks
             (id integer, date_created real, description text, is_done integer)''')

connection.commit()
connection.close()