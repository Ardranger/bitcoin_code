#!/usr/bin/env python3

import sqlite3
import pandas as pd
from dumb_buy import one_min_trading_phemex


conn = sqlite3.connect("/mnt/external_hdd/Data/coinbase.db")
df = pd.read_sql_query("SELECT * FROM bitcoin_coinbase", conn)
conn.close()

df['datetime'] = pd.to_datetime(df['datetime'], format='%Y-%m-%d %H:%M:%S')


bitcoin_wallet=0
usd_wallet=100
previous_price=0
current_price=0

hodl_position_start = df['price'].iloc[0] 
hodl_position_end = df['price'].iloc[-1]
hodl_profit= hodl_position_end/hodl_position_start*100
print("Hodl outcome " + str(hodl_profit) + "%")


for index,row in df.iterrows():
    current_price = row[1]
    usd_wallet,bitcoin_wallet=one_min_trading_phemex(current_price,previous_price,usd_wallet,bitcoin_wallet)
    previous_price=current_price
    


