
/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/
SELECT DISTINCT CITY
FROM STATION
WHERE
UPPER(CITY) LIKE '%A' OR
UPPER(CITY) LIKE '%E' OR
UPPER(CITY) LIKE '%I' OR
UPPER(CITY) LIKE '%O' OR
UPPER(CITY) LIKE '%U';