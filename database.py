import sqlite3 as lite
import pandas as pd
import collections

con = lite.connect('getting_started.db')
cities = (('New York City', 'NY'), ('Boston', 'MA'), ('Chicago', 'IL'))
weather = (('New York City', 2013, 'July', 'January', 63), ('Boston', 2013, 'July', 'January', 59), ('Chicago', 2013, 'July', 'January', 54))

with con:
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS cities')
    cur.execute('DROP TABLE IF EXISTS weather')
    cur.execute('CREATE TABLE cities (name text, state text)')
    cur.execute('CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer)')

    cur.executemany('INSERT INTO cities VALUES(?,?)', cities)
    cur.executemany('INSERT INTO weather VALUES(?,?,?,?,?)', weather)

    cur.execute('SELECT name, state, city, year, warm_month, cold_month, average_high FROM cities INNER JOIN weather on name = city')
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]

    df = pd.DataFrame(rows, columns=cols)

    july_cities = []
    for row in rows:
        if row[4] == 'July':
            july_cities.append(row[0] + ", " + row[1] )

    print('The cities that are warmest in July are: ' + ', '.join(str(city) for city in july_cities))
