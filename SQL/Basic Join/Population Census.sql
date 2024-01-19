/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
select sum(city.population)
from city inner join country on city.countryCode=country.Code where country.continent='Asia'
