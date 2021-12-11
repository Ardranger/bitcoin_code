import sqlite3
import pandas as pd
#import matplotlib
#matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt



conn = sqlite3.connect("/mnt/external_hdd/Data/uber.db")
df = pd.read_sql_query("SELECT * FROM bitcoin_coinbase", conn)
conn.close()

#print(df.dtypes)
#print(df.info)
#print(type(df['datetime'][0]))
#plt.plot(df["datetime"],["price"])
#print(df["price"])
#print(df["datetime"])
df['datetime'] = pd.to_datetime(df['datetime'], format='%Y-%m-%d %H:%M:%S')
#print(df["datetime"])
plt.plot(df["datetime"],df["price"])
plt.suptitle('Bitcoin Price (USD)')
plt.show()

