import sqlite3
from faker import Faker
import random
from datetime import datetime

# Создание базы данных и подключение к ней
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Создание таблиц
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        group_id INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        teacher_id INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject_id INTEGER,
        grade INTEGER,
        date TEXT
    )
''')

# Используем Faker для заполнения данных
fake = Faker()

# Заполнение таблицы групп
groups = ['Group A', 'Group B', 'Group C']
for group in groups:
    cursor.execute('INSERT INTO groups (name) VALUES (?)', (group,))

# Заполнение таблицы преподавателей
teachers = [fake.name() for _ in range(5)]
for teacher in teachers:
    cursor.execute('INSERT INTO teachers (name) VALUES (?)', (teacher,))

# Заполнение таблицы предметов
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'Literature', 'Art']
for subject in subjects:
    cursor.execute('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', (subject, random.choice(range(1, 6))))

# Заполнение таблицы студентов
for _ in range(50):
    cursor.execute('INSERT INTO students (name, group_id) VALUES (?, ?)', (fake.name(), random.choice(range(1, 4))))

# Заполнение таблицы оценок
for student_id in range(1, 51):
    for subject_id in range(1, 9):
        for _ in range(random.randint(10, 20)):
            date_str = fake.date_this_year().strftime('%Y-%m-%d')
            cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)', 
                           (student_id, subject_id, random.randint(1, 100), date_str))

conn.commit()
conn.close()
