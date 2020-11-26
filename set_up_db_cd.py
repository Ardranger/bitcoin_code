#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect("/mnt/external_hdd/Data/coindesk.db")
c = conn.cursor()

c.execute('''CREATE TABLE bitcoin_coinbase
             (datetime text, price real)''')

conn.commit()
