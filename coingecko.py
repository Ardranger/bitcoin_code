import requests
import datetime
import json
import time
import sqlite3 



def setup_db_coingecko(parsed):
    conn = sqlite3.connect("/mnt/external_hdd/Data/coingecko.db")
    c = conn.cursor()
    for coin_name in parsed:
        #print(timestamp)
        conn.execute("CREATE TABLE IF NOT EXISTS " + str(coin_name) + " (datetime text, price float, market_cap float, last_update float, day_vol float)")
    conn.commit()
    conn.close()


def main():
    # "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Clitecoin%2Cethereum%2Cbinancecoin%2CCardano%2CTether%2CPolkadot%2CXRP&vs_currencies=usd%2Ceur&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true"
    coins="bitcoin,litecoin,ethereum,binancecoin,Cardano,Polkadot,XRP"
    api_base_url = "https://api.coingecko.com/api/v3/simple/price?"
    # "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Clitecoin%2Cethereum%2Cbinancecoin%2CCardano%2CTether%2CPolkadot%2CXRP&vs_currencies=usd%2Ceur&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true"
    requested_coins = "ids=bitcoin%2Clitecoin%2Cethereum%2Cbinancecoin%2CCardano%2CPolkadot%2CXRP"
    requested_fiat = "&vs_currencies=usd"
    requested_fields = "&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true"

    api_call = api_base_url + requested_coins + requested_fiat+ requested_fields
    print(api_call)
    timestamp = datetime.datetime.now()
    r = requests.get(api_call)
    parsed = json.loads(r.text)
    #print(json.dumps(parsed, indent=4, sort_keys=True))
    #setup_db_coingecko(parsed)
    for coin_name in parsed:
        #print(timestamp)
        conn = sqlite3.connect("/mnt/external_hdd/Data/coingecko.db")
        c = conn.cursor()
        c.execute("INSERT INTO "+str(coin_name) +" VALUES (?, ?, ?, ?, ?);",(timestamp,parsed[coin_name]["usd"],parsed[coin_name]["usd_market_cap"],parsed[coin_name]["last_updated_at"],parsed[coin_name]["usd_24h_vol"]))
        conn.commit()
        conn.close()




if __name__ == "__main__":

    main()