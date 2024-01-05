/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

SELECT
   CASE WHEN grades.grade >= 8 THEN students.name ELSE NULL END AS student_name,
   grades.grade,
   marks
FROM students
JOIN grades ON students.marks >= grades.min_mark AND students.marks <= grades.max_mark
ORDER BY
    grades.grade desc,
    case when grades.grade >=8 then students.name
    end ASC,
    CASE WHEN grades.grade < 8 THEN students.marks
    end asc
