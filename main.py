import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

def execute_query_from_file(filename, params=None):
    with open(filename, 'r') as file:
        query = file.read()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    return cursor.fetchall()

subject_id_param = 1  
group_id_param = 1  
teacher_id_param = 1  
student_id_param = 1  

results_query_1 = execute_query_from_file('queries/query_1.sql')
results_query_2 = execute_query_from_file('queries/query_2.sql', params=(subject_id_param,))
results_query_3 = execute_query_from_file('queries/query_3.sql', params=(subject_id_param,))
results_query_4 = execute_query_from_file('queries/query_4.sql')
results_query_5 = execute_query_from_file('queries/query_5.sql', params=(teacher_id_param,))
results_query_6 = execute_query_from_file('queries/query_6.sql', params=(group_id_param,))
results_query_7 = execute_query_from_file('queries/query_7.sql', params=(group_id_param, subject_id_param))
results_query_8 = execute_query_from_file('queries/query_8.sql', params=(teacher_id_param,))
results_query_9 = execute_query_from_file('queries/query_9.sql', params=(student_id_param,))
results_query_10 = execute_query_from_file('queries/query_10.sql', params=(student_id_param, teacher_id_param))

def print_results(query_num, results, limit=10):
    print(f"\nResults of Query {query_num}:")
    count = 0
    if query_num in {1, 2, 3}:
        for name, avg_grade in results:
            if count < limit:
                print(f"Student: {name}, Average Grade: {avg_grade:.2f}")
            count += 1
    elif query_num == 4:
        for avg_grade in results:
            print(f"Average Grade: {avg_grade[0]:.2f}")
    elif query_num == 8:
        for avg_grade in results:
            print(f"Average Grade given by the teacher: {avg_grade[0]:.2f}")
    elif query_num in {5, 9, 10}:
        unique_courses = set()
        for course in results:
            unique_courses.add(course[0])
        for course in unique_courses:
            if count < limit:
                print(f"Course: {course}")
            count += 1
    elif query_num == 6:
        for student in results:
            if count < limit:
                print(f"Student: {student[0]}")
            count += 1
    elif query_num == 7:
        for name, grade in results:
            if count < limit:
                print(f"Student: {name}, Grade: {grade}")
            count += 1
    if count > limit:
        print(f"...and {count - limit} more rows")

print_results(1, results_query_1)
print_results(2, results_query_2)
print_results(3, results_query_3)
print_results(4, results_query_4)
print_results(5, results_query_5)
print_results(6, results_query_6)
print_results(7, results_query_7)
print_results(8, results_query_8)
print_results(9, results_query_9)
print_results(10, results_query_10)

conn.close()
