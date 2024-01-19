/*
Enter your query here.
*/

SELECT Name as subs
FROM STUDENTS
WHERE Marks > 75
ORDER BY SUBSTRING(Name, length(Name)-2, 3) , id asc;