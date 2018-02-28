sql_zoo_sel_within_sel (https://sqlzoo.net/wiki/SELECT_within_SELECT_Tutorial)


/* question 1
List each country name where the population is larger than that of 'Russia'.
*/
SELECT name FROM world
  WHERE population >
     (SELECT population FROM world
      WHERE name='Russia')

/* question 2
Show the countries in Europe with a per capita GDP greater than 'United Kingdom'.
*/
select 
  name
from
  world
where
  gdp/population > 
(select gdp/population from world where name = 'United Kingdom')
and
  continent = 'Europe'
  
/* question 3
List the name and continent of countries in the continents containing either Argentina
or Australia. Order by name of the country.
*/

select 
  name, continent
from
  world
where
  continent in (select continent from world where name = 'Argentina' or name = 'Australia')
order by
  name
  
/* question 4
Which country has a population that is more than Canada but less than Poland?
Show the name and the population.
*/

select
  name, population
from
  world
where
  population > (select population from world where name = 'Canada')
and
  population < (select population from world where name = 'Poland')
  
/* question 5 
Show the name and the population of each country in Europe. Show the population as
a percentage of the population of Germany.
*/

select
  name, concat(round(100*population/(select population from world where name = 'Germany'),0),'%')
from
  world
where
  continent = 'Europe'
  
/* question 6
Which countries have a GDP greater than every country in Europe?
[Give the name only.] (Some countries may have NULL gdp values)
*/

select
  name
from
  world
where
  gdp > (select max(gdp) from world where continent = 'Europe')
and
  gdp is not null
  
/* question 7

