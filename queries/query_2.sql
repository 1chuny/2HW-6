-- query_2.sql
SELECT students.name, AVG(grades.grade) as average_grade
FROM grades
JOIN students ON grades.student_id = students.id
WHERE grades.subject_id = ?
GROUP BY students.id
ORDER BY average_grade DESC
LIMIT 1;
