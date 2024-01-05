/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

Select city.name from city inner join country on city.countrycode=country.code where country.continent='Africa'