import subprocess
import sqlite3
import pandas as pd


def sync_dbs():
    bash_subprocess = subprocess.run("scp -i ~/.ssh/ssh-key-2020-11-24.key opc@132.145.55.214:/home/opc/Data/coindesk.db /tmp/db_vm1", shell=True)
    
    bash_subprocess = subprocess.run("scp -i ~/.ssh/ssh-key-2021-01-28.key opc@132.145.78.50:/home/opc/Data/coindesk.db /tmp/db_vm2", shell=True)


def merge():
    vm1_df = load_db_to_df("/tmp/db_vm1")
    #print(vm1_df)
    
    vm2_df = load_db_to_df("/tmp/db_vm2")
    #print(vm2_df)

    rpi_df = load_db_to_df("/mnt/external_hdd/Data/coindesk.db")
    #print(rpi_df)

    uber_df = pd.concat([vm1_df,vm2_df,rpi_df])
    print(uber_df)


def load_db_to_df(path_to_sqlite_db):

    conn = sqlite3.connect(path_to_sqlite_db)
    df = pd.read_sql_query("SELECT * FROM bitcoin_coinbase", conn)
    conn.close()
    return df


if __name__ == "__main__":
    #sync_dbs()
    merge()