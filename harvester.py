#!/usr/bin/env python3
import requests
import json
import datetime
import sqlite3
import time


def pull_from_coinbase():
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        parsed = json.loads(r.text)
        current_price = float(parsed["bpi"]["USD"]["rate_float"])
        timestamp=parsed["time"]["updatedISO"]
        date_time_obj = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S+00:00")
        return date_time_obj,current_price;


def harvest():
    conn = sqlite3.connect("/mnt/external_hdd/Data/coindesk.db")
    c = conn.cursor()
    date_time_obj,cuurent_price =pull_from_coinbase()
    c.execute("INSERT INTO bitcoin_coinbase VALUES (?, ?);",(date_time_obj,cuurent_price))
    conn.commit()
    conn.close()
  
harvest()
