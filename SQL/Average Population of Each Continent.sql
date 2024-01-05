/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

Select COUNTRY.Continent,Avg(city.population) from Country join city on country.code=city.countrycode group by COUNTRY.Continent;