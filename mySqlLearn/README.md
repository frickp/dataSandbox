# Description
Code to get a mysql database of life expectancy/GNP of different countries. From [this site](http://moderndata.plot.ly/graph-data-from-mysql-database-in-python/).

### Bash scripts to get the data
sudo mysql -uroot
wget http://downloads.mysql.com/docs/world.sql.zip
unzip world.sql.zip

### mysql scripts to create/load the database 
CREATE DATABASE world;
USE world;
SOURCE /home/ubuntu/world.sql;

###  Now in python
import MySQLdb
conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="world")
cursor = conn.cursor()

queryAll = 'select Name, Continent, Population, LifeExpectancy, GNP from Country'
df = pd.read_sql(queryAll,conn)
