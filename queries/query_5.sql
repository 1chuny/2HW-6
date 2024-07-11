-- query_5.sql
SELECT subjects.name
FROM subjects
WHERE subjects.teacher_id = ?;
