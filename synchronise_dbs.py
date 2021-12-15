import subprocess
import sqlite3
import pandas as pd


def sync_dbs():
    print("Downloading remote sqlite databases")
    bash_subprocess = subprocess.run("scp -i ~/.ssh/ssh-key-2020-11-24.key opc@132.145.55.214:/home/opc/Data/coindesk.db /tmp/db_vm1.db", shell=True)
    
    bash_subprocess = subprocess.run("scp -i ~/.ssh/ssh-key-2021-01-28.key opc@132.145.78.50:/home/opc/Data/coindesk.db /tmp/db_vm2.db", shell=True)


def merge():
    
    print("Loading sqlite dbs from listeners to memory")

    vm1_df = load_db_to_df("/tmp/db_vm1.db")
    vm2_df = load_db_to_df("/tmp/db_vm2.db")
    rpi_df = load_db_to_df("/mnt/external_hdd/Data/coindesk.db")

    uber_df = pd.concat([vm1_df,vm2_df,rpi_df])
    
    #Convert  strs in "datetime" col to datetime objects for sort to work
    uber_df['datetime'] = pd.to_datetime(uber_df['datetime'], format='%Y-%m-%d %H:%M:%S')
    uber_df = uber_df.sort_values(by=["datetime"])
    print("Dropping duplicates...")
    uber_df = uber_df.drop_duplicates()
    uber_df = uber_df.set_index('datetime').resample('1T').mean().interpolate('linear')
    uber_df = uber_df.reset_index()

    print("Saving merged dataframe into sqlite database at path /mnt/external_hdd/Data/uber.db")
    conn = sqlite3.connect('/mnt/external_hdd/Data/uber.db') 
    c = conn.cursor()


    #Set up table in file if not found
    c.execute('''CREATE TABLE IF NOT EXISTS bitcoin_coinbase
             (datetime text, price real)''')
    conn.commit()
    conn.close()

    #Connect to sqlite
    conn = sqlite3.connect('/mnt/external_hdd/Data/uber.db') 
    c = conn.cursor()
    uber_df.to_sql('bitcoin_coinbase', conn, if_exists='replace', index = False)
    conn.commit()
    conn.close()

def load_db_to_df(path_to_sqlite_db):

    conn = sqlite3.connect(path_to_sqlite_db)
    df = pd.read_sql_query("SELECT * FROM bitcoin_coinbase", conn)
    conn.close()
    return df


if __name__ == "__main__":
    sync_dbs()
    merge()