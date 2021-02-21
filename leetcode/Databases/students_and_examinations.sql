# Write your MySQL query statement below
select
    Students.*
    , Subjects.*
    , IFNULL(exams_count.attended_exams, 0) AS attended_exams
FROM Students
CROSS JOIN Subjects
LEFT JOIN (
    SELECT
        student_id
        , subject_name
        , count(*) AS attended_exams
    FROM Examinations
    GROUP BY student_id, subject_name
) exams_count
ON Students.student_id = exams_count.student_id
AND Subjects.subject_name = exams_count.subject_name
ORDER BY student_id, subject_name;
