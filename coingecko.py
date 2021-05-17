import requests
import datetime
import json
import time
import sqlite3 
import yaml

def setup_db_coingecko(parsed,db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    for coin_name in parsed:
        #print(timestamp)
        conn.execute("CREATE TABLE IF NOT EXISTS " + str(coin_name) + " (datetime text, price float, market_cap float, last_update float, day_vol float)")
    conn.commit()
    conn.close()




def main():
    coins="bitcoin,litecoin,ethereum,binancecoin,Cardano,Polkadot,XRP"
    api_base_url = "https://api.coingecko.com/api/v3/simple/price?"
    db_path = "/mnt/external_hdd/Data/coingecko.db"
    path=__file__.split('/')
    new_path=path[:-1] + ["coin_config.yaml"]
    read_file_name = '/'.join(new_path)

    with open(read_file_name) as file:
        coin_list = yaml.full_load(file)
        requested_coins = "ids=" + ("%2C").join(coin_list["coins"])
    
    requested_fiat = "&vs_currencies=usd"
    requested_fields = "&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true"
    api_call = api_base_url + requested_coins + requested_fiat+ requested_fields
    timestamp = datetime.datetime.now()
    r = requests.get(api_call)
    parsed = json.loads(r.text)
    
    try:
        for coin_name in parsed:
            #print(timestamp)
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("INSERT INTO "+str(coin_name) +" VALUES (?, ?, ?, ?, ?);",(timestamp,parsed[coin_name]["usd"],parsed[coin_name]["usd_market_cap"],parsed[coin_name]["last_updated_at"],parsed[coin_name]["usd_24h_vol"]))
            conn.commit()
            conn.close()
    except:
        setup_db_coingecko(parsed,db_path)
        for coin_name in parsed:
            #print(timestamp)
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            c.execute("INSERT INTO "+str(coin_name) +" VALUES (?, ?, ?, ?, ?);",(timestamp,parsed[coin_name]["usd"],parsed[coin_name]["usd_market_cap"],parsed[coin_name]["last_updated_at"],parsed[coin_name]["usd_24h_vol"]))
            conn.commit()
            conn.close()




if __name__ == "__main__":

    main()
