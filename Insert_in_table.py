# БД зачит да?
import sqlite3

connection = sqlite3.connect('toDO.db')
cursor = connection.cursor()

new_quasks = [(1, '2020-10-05', 'Помыть посуду', 1),
              (2, '2020-10-05', 'Слепить вареники', 1),
              (3, '2020-10-05', 'Написать номальный скрипт для занесения данных в таблицу', 0),
             ]

cursor.executemany('INSERT INTO quasks VALUES (?,?,?,?)', new_quasks)
connection.close()