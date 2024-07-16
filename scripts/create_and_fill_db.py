import sqlite3
from faker import Faker
import random
from datetime import datetime

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

cursor.execute('PRAGMA foreign_keys = ON')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teachers(id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject_id INTEGER,
        grade INTEGER NOT NULL,
        date TEXT NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students(id)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
        FOREIGN KEY (subject_id) REFERENCES subjects(id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    )
''')


fake = Faker()

groups = ['Group A', 'Group B', 'Group C']
for group in groups:
    cursor.execute('INSERT INTO groups (name) VALUES (?)', (group,))

teachers = [fake.name() for _ in range(5)]
for teacher in teachers:
    cursor.execute('INSERT INTO teachers (name) VALUES (?)', (teacher,))

subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'Literature', 'Art']
teacher_ids = [row[0] for row in cursor.execute('SELECT id FROM teachers')]
for subject in subjects:
    cursor.execute('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', (subject, random.choice(teacher_ids)))

group_ids = [row[0] for row in cursor.execute('SELECT id FROM groups')]
for _ in range(50):
    cursor.execute('INSERT INTO students (name, group_id) VALUES (?, ?)', (fake.name(), random.choice(group_ids)))

student_ids = [row[0] for row in cursor.execute('SELECT id FROM students')]
subject_ids = [row[0] for row in cursor.execute('SELECT id FROM subjects')]
for student_id in student_ids:
    for subject_id in subject_ids:
        for _ in range(random.randint(10, 20)):
            date_str = fake.date_this_year().strftime('%Y-%m-%d')
            cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)', 
                           (student_id, subject_id, random.randint(1, 100), date_str))

conn.commit()
conn.close()
