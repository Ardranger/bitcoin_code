#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect("coinbase.db")
timestamp="2020-11-12T22:36:00+00:00"
price=16327.9983
date_time_obj = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S+00:00")
c = conn.cursor()

c.execute('''CREATE TABLE bitcoin_coinbase
             (datetime text, price real)''')

c.execute("INSERT INTO bitcoin_coinbase VALUES (?, ?);", (date_time_obj,  ))

c.execute("INSERT INTO bitcoin_coinbase VALUES ('2020-11-12T22:36:00+00:00',)16,327.9983")

conn.commit()

conn.close()

#for row in c.execute('SELECT * FROM bitcoin_coinbase ORDER BY price'):
#    print(row)

