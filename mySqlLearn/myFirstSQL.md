Title: MyFIRST MySQL
Date: 2015-12-09 10:20
Modified: 2015-12-09 19:30
Category: blog
Tags: MySQL, data science
Slug: myfirst-mysql
Authors: Peter Frick
Summary: I've looked at a couple tutorials on SQL, but the best way to learn is to play around right? Let's get started.

# Description
Code to get a mysql database of life expectancy/GNP of different countries. From [this site](http://moderndata.plot.ly/graph-data-from-mysql-database-in-python/).

### Bash scripts to get the data

```
sudo mysql -uroot
wget http://downloads.mysql.com/docs/world.sql.zip
unzip world.sql.zip
```

### mysql scripts to create/load the database
```
CREATE DATABASE world;
USE world;
SOURCE /home/ubuntu/world.sql;
```
###  Now in python
import MySQLdb
conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="world")
cursor = conn.cursor()

queryAll = 'select Name, Continent, Population, LifeExpectancy, GNP from Country'
df = pd.read_sql(queryAll,conn)

select distinct CountryCode, name from city where Population > 5000000;