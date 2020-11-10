#!/usr/bin/env python3

import time
import requests
import json
import pyfiglet
#https://api.coindesk.com/v1/bpi/currentprice.json

result = pyfiglet.figlet_format("Live bitcoin ticker") 
print(result) 


while True:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    #print(r)
    parsed = json.loads(r.text)
    #print(json.dumps(parsed, indent=4, sort_keys=True))
    print("Bitcoin value: $" + parsed["bpi"]["USD"]["rate"] + " - " +  parsed["time"]["updateduk"])
    #print("Time of price change: " + parsed["time"]["updateduk"])
    time.sleep(60)
