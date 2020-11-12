#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect("coinbase.db")

c = conn.cursor()

c.execute('''CREATE TABLE bitcoin_coinbase
             (datetime text, price real)''')

#c.execute("INSERT INTO bitcoin_coinbase VALUES ('2006-01-05',35.14)")

conn.commit()

conn.close()

#for row in c.execute('SELECT * FROM bitcoin_coinbase ORDER BY price'):
#    print(row)

