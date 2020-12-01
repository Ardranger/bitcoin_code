import sqlite3
import pandas as pd
import dumb_buy.py


conn = sqlite3.connect("/mnt/external_hdd/Data/coinbase.db")
df = pd.read_sql_query("SELECT * FROM bitcoin_coinbase", conn)
conn.close()

df['datetime'] = pd.to_datetime(df['datetime'], format='%Y-%m-%d %H:%M:%S')

print(df['price'])

for index,row in df.iterrows():
	print(row[1])

