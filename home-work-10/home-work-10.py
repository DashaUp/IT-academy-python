import sqlite3
import time
from weather import getTemperature

unix_time = int(time.time())
# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Weather (

id INTEGER PRIMARY KEY,
date INTEGER ,
temperature INTEGER
)
''')

# Сохраняем изменения и закрываем соединение
connection.commit()


cursor.execute('INSERT INTO Weather (date, temperature) VALUES (?, ?)', (unix_time, getTemperature()))

connection.commit()
connection.close()