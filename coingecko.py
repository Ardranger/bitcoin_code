import requests
import datetime
import json


coins="bitcoin,litecoin,ethereum,binancecoin,Cardano,Tether,Polkadot,XRP"
#api_base_url = "https://api.coingecko.com/api/v3/simple/price?"
api_base_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Clitecoin%2Cethereum%2Cbinancecoin%2CCardano%2CTether%2CPolkadot%2CXRP&vs_currencies=usd%2Ceur&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true"


r = requests.get(api_base_url)
print(r.text)