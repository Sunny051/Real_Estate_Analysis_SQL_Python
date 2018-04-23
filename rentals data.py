import mysql.connector
cnx = mysql.connector.connect(user='scott', password='pwd123', host='localhost', database='zillow')
cursor = cnx.cursor()
#1
query1  = ("SELECT COUNT(DISTINCT citycode) AS num_of_cities FROM city")
cursor.execute(query1)
for(num_of_cities)in cursor:print("{}".format(num_of_cities))

query2 = ("SELECT COUNT(DISTINCT state) AS num_0f_states FROM city")
cursor.execute(query2)
for(num_of_states)in cursor:print("{}".format(num_of_states))
#2
query3=("SELECT AVG(price) AS avg_price FROM city_price")
cursor.execute(query3)
for(avg_price)in cursor:print("{}".format(avg_price))

query4=("SELECT MIN(price) AS min_price FROM city_price")
cursor.execute(query4)
for(min_price)in cursor:print("{}".format(min_price))

query5=("SELECT MAX(price) as max_price FROM city_price")
cursor.execute(query5)
for(max_price)in cursor:print("{}".format(max_price))
#3
query6=("SELECT AVG(pricesqft) AS avg_pricesqft FROM city_pricepersqft")
cursor.execute(query6)
for(avg_pricesqft)in cursor:print("{}".format(avg_pricesqft))

query7=("SELECT MIN(pricesqft) AS min_pricesqft FROM city_pricepersqft")
cursor.execute(query7)
for(min_pricesqft)in cursor:print("{}".format(min_pricesqft))

query8=("SELECT MAX(pricesqft) AS max_pricesqft FROM city_pricepersqft")
cursor.execute(query8)
for(max_pricesqft)in cursor:print("{}".format(max_pricesqft))

#4
query9=("SELECT AVG(pricesqft) AS avg_pricesqft_OK FROM city_pricepersqft JOIN city on city.citycode = city_pricepersqft.city_citycode WHERE state = 'OK'")
cursor.execute(query9)
for(avg_pricesqft_OK)in cursor:print("{}".format(avg_pricesqft_OK))

#5
query10=("SELECT COUNT(metro) AS metro_num FROM (SELECT metro, AVG(pricesqft) as avg_pricesqft_metro FROM city_pricepersqft JOIN city on citycode = city_citycode GROUP by metro HAVING avg_pricesqft_metro > (SELECT AVG(pricesqft) AS avg_pricesqft_OK FROM city_pricepersqft JOIN city on city.citycode = city_pricepersqft.city_citycode WHERE state = 'OK')) AS metro_ok")
cursor.execute(query10)
for(metro_num)in cursor:print("{}".format(metro_num))

#6
query11=("SELECT metro, city FROM city_pricepersqft JOIN city on citycode = city_citycode GROUP by metro HAVING AVG(pricesqft) > (SELECT AVG(pricesqft) AS avg_pricesqft_OK FROM city_pricepersqft JOIN city on city.citycode = city_pricepersqft.city_citycode WHERE state = 'OK')")
cursor.execute(query11)
for(metro,city)in cursor:print("{},{}".format(metro,city))






