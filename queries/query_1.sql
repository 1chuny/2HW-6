-- query_1.sql
SELECT students.name, AVG(grades.grade) as average_grade
FROM grades
JOIN students ON grades.student_id = students.id
GROUP BY students.id
ORDER BY average_grade DESC
LIMIT 5;
