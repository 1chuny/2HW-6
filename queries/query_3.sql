-- query_3.sql
SELECT groups.name, AVG(grades.grade) as average_grade
FROM grades
JOIN students ON grades.student_id = students.id
JOIN groups ON students.group_id = groups.id
WHERE grades.subject_id = ?
GROUP BY groups.id;
