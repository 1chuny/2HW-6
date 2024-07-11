-- query_8.sql
SELECT AVG(grades.grade) as average_grade
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.teacher_id = ?;
