import sqlite3

#Підключення до бази даних
connection = sqlite3.connect('university.db')
cursor = connection.cursor()

#Створення таблиці
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER,
                    major TEXT
                )''')

#Створення таблиці
cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    course_name TEXT,
                    teacher TEXT
                )''')

