import yaml

with open(r'coin_config.yaml') as file:
    coin_list = yaml.full_load(file)
    print(coin_list["coins"])