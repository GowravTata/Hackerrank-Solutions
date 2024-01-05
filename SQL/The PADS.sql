/*
Enter your query here.
*/
select concat(name ,'(',substr(occupation,1,1),')')as new_name
from occupations
order by name;

select concat('There are a total of ',count(*),' ', lower(occupation), 's.' ) as occupation_info
from occupations
group by occupation
order by count(*);