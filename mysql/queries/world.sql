USE world;

###########################################################################################
#	1. What query would you run to get all the countries that speak Slovene? Your query should 
#	return the name of the country, language and language percentage. Your query should arrange
#	the result by language percentage in descending order. 

SELECT country.Name as name, countrylanguage.Language as language, countrylanguage.Percentage as percentage  FROM country
LEFT JOIN countrylanguage ON country.code=countrylanguage.CountryCode
WHERE Language = "Slovene"
ORDER BY Percentage DESC
;


###########################################################################################
# 	2. What query would you run to display the total number of cities for each country? 
# 	Your query should return the name of the country and the total number of cities. 
# 	Your query should arrange the result by the number of cities in descending order. 

SELECT countries.name, COUNT(country_id) AS cities FROM countries
LEFT JOIN cities ON countries.id=cities.country_id
GROUP BY name
ORDER BY COUNT(country_id) DESC
;

###########################################################################################
#	3. What query would you run to get all the cities in Mexico with a population of greater 
#	than 500,000? Your query should arrange the result by population in descending order. 

SELECT cities.name, cities.population, cities.country_id FROM countries
LEFT JOIN cities ON countries.ID=cities.country_id
WHERE countries.name = "Mexico" AND cities.population >= 500000
ORDER BY population DESC
;

###########################################################################################

#	4. What query would you run to get all languages in each country with a percentage greater 
#	than 89%? Your query should arrange the result by percentage in descending order. 

SELECT countries.name, languages.language, languages.percentage FROM countries
LEFT JOIN languages ON countries.id=languages.country_id
ORDER BY percentage DESC
;

###########################################################################################
#	5. What query would you run to get all the countries with Surface Area below 501 
#	and Population greater than 100,000? 

SELECT country.Name, country.Population, country.SurfaceArea FROM country
WHERE SurfaceArea <= 501 AND Population > 100000
;

###########################################################################################
#	6. What query would you run to get countries with only Constitutional Monarchy 
#	with a capital greater than 200 and a life expectancy greater than 75 years? 

SELECT country.name, country.GovernmentForm , country.Capital, country.LifeExpectancy FROM country
WHERE GovernmentForm = "Constitutional Monarchy" AND Capital > 200 AND LifeExpectancy > 75
;

###########################################################################################
#	7. What query would you run to get all the cities of Argentina inside the 
#	Buenos Aires district and have the population greater than 500, 000? 
#	The query should return the Country Name, City Name, District and Population.

SELECT countries.name, cities.name, cities.district, cities.population  FROM countries
LEFT JOIN cities ON countries.ID=cities.country_id
WHERE countries.name = "Argentina" AND cities.district = "Buenos Aires" AND cities.population > 500000
;


###########################################################################################
#	8. What query would you run to summarize the number of countries in each region? 
#	The query should display the name of the region and the number of countries. 
#	Also, the query should arrange the result by the number of countries in descending order.

SELECT country.Region, count(Region) AS number_of_countries FROM country
GROUP BY Region
ORDER BY number_of_countries DESC
;

