#!/usr/bin/env python3

import time
import requests
import json
import pyfiglet
#https://api.coindesk.com/v1/bpi/currentprice.json
import sqlite3

def main():
    result = pyfiglet.figlet_format("Live bitcoin ticker") 
    print(result) 
    usd_wallet=100
    bitcoin_wallet=0
    pricerise=False
    current_price=0
    previous_price=0
    

    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    parsed = json.loads(r.text)
    inital_price = float(parsed["bpi"]["USD"]["rate_float"])
    buy_and_hold_bitcoin=100/inital_price
    
    conn = sqlite3.connect("coinbase.db")
    c = conn.cursor()

    
    
    while True:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        parsed = json.loads(r.text)
        current_price = float(parsed["bpi"]["USD"]["rate_float"])
        print("Bitcoin value: $" + parsed["bpi"]["USD"]["rate"] + " - " +  parsed["time"]["updateduk"])
        usd_wallet,bitcoin_wallet=one_min_trading(current_price,previous_price,usd_wallet,bitcoin_wallet)
        previous_price=current_price
        print("Dumb trading assets $" + str(current_price*bitcoin_wallet + usd_wallet ) + ": Buy and hold assets $" + str(current_price*buy_and_hold_bitcoin)) 
        datetime_stamp=parsed["time"]["updateduk"]
        time.sleep(60)


def one_min_trading(current_price,previous_price,usd_wallet,bitcoin_wallet):
        if (current_price > previous_price) and (usd_wallet != 0):
            bitcoin_wallet=usd_wallet/current_price
            print("Bought BT " + str(bitcoin_wallet))
            usd_wallet=0
        elif (current_price < previous_price) and (bitcoin_wallet != 0):
            usd_wallet=current_price*bitcoin_wallet
            print("Bought $" + str(usd_wallet))
            bitcoin_wallet=0
        else:
            print("No change")
        return usd_wallet,bitcoin_wallet;

if __name__ == "__main__":
    # execute only if run as a script
    main()
