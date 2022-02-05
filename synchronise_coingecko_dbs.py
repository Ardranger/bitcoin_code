import subprocess
import sqlite3
from turtle import st
import pandas as pd
import yaml

def sync_dbs():
    bash_subprocess = subprocess.run("scp -i ~/.ssh/ssh-key-2020-11-24.key opc@132.145.55.214:/home/opc/Data/coingecko.db /tmp/coingecko_db_vm1.db", shell=True)
    
    bash_subprocess = subprocess.run("scp -i ~/.ssh/ssh-key-2021-01-28.key opc@132.145.78.50:/home/opc/Data/coingecko.db /tmp/coingecko_db_vm2.db", shell=True)

    bash_subprocess = subprocess.run("cp /mnt/external_hdd/Data/coingecko.db  /tmp/coingecko_db_rpi.db", shell=True)

def merge(coin_name):
    try: 
        vm1_df = load_db_to_df("/tmp/coingecko_db_vm1.db",coin_name)
        print("Loaded from vm1 for " + str(coin_name))
    except Exception as e:
        print(e)
        print("Load failed on vm1 for " + str(coin_name))
        vm1_df = pd.DataFrame()


    try: 
        vm2_df = load_db_to_df("/tmp/coingecko_db_vm2.db",coin_name)
        print("Loaded from vm2 for " + str(coin_name))
    except Exception as e:
        print(e)
        print("Load failed on vm2 for " + str(coin_name))
        vm2_df = pd.DataFrame()

  
    try: 
        rpi_df = load_db_to_df("/tmp/coingecko_db_rpi.db",coin_name)
        print("Loaded from rpi4 for " + str(coin_name))
    except Exception as e:
        print(e)
        print("Load failed on rpi4 for " + str(coin_name))
        rpi_df = pd.DataFrame()



    if ((vm1_df.empty) and (vm2_df.empty) and (rpi_df.empty)):
        print("No successful load, ending merge for " + str(coin_name))
        return 
    else: 
        print("Merging dbs for " + str(coin_name)) 

    uber_df = pd.concat([vm1_df,vm2_df,rpi_df])
    
    #Convert  strs in "datetime" col to datetime objects for sort to work
    uber_df['datetime'] = pd.to_datetime(uber_df['datetime'], format='%Y-%m-%d %H:%M:%S')
    uber_df = uber_df.sort_values(by=["datetime"])
    uber_df = uber_df.drop_duplicates()
    uber_df = uber_df.set_index('datetime').resample('1T').mean().interpolate('linear')
    uber_df = uber_df.reset_index()

    path=__file__.split('/')
    new_path=path[:-1] + ["coin_config.yaml"]
    read_file_name = '/'.join(new_path)

    with open(read_file_name) as file:
        coin_list = yaml.full_load(file)
        coin_list = coin_list["coins"]

    conn = sqlite3.connect('/mnt/external_hdd/Data/coingecko_uber.db') 
    c = conn.cursor()
    conn.execute("CREATE TABLE IF NOT EXISTS " + str(coin_name) + " (datetime text, price float, market_cap float, last_update float, day_vol float)")
    conn.commit()
    conn.close()

    conn = sqlite3.connect('/mnt/external_hdd/Data/coingecko_uber.db') 
    c = conn.cursor()
    uber_df.to_sql(coin_name, conn, if_exists='replace', index = False)
    conn.commit()
    conn.close()
    print("Merged " + str(coin_name))

def load_db_to_df(path_to_sqlite_db, coin_name):

    conn = sqlite3.connect(path_to_sqlite_db)
    df = pd.read_sql_query("SELECT * FROM " + str(coin_name), conn)
    conn.close()
    return df


if __name__ == "__main__":
    #sync_dbs()

    path=__file__.split('/')
    new_path=path[:-1] + ["coin_config.yaml"]
    read_file_name = '/'.join(new_path)

    with open(read_file_name) as file:
        coin_list = yaml.full_load(file)
        coin_list = coin_list["coins"]

    for coin_name in coin_list:
        print(coin_name)
        merge(coin_name)
        
   