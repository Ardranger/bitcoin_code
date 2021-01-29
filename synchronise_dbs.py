import subprocess
import sqlite3
import pandas as pd


def sync_dbs():
    bash_subprocess = subprocess.run("scp -i ~/.ssh/ssh-key-2020-11-24.key opc@132.145.55.214:/home/opc/Data/coindesk.db /tmp/db_vm1", shell=True)
    
    bash_subprocess = subprocess.run("scp -i ~/.ssh/ssh-key-2021-01-28.key opc@132.145.78.50:/home/opc/Data/coindesk.db /tmp/db_vm2", shell=True)

    bash_subprocess = subprocess.run("scp -i ~/.ssh/ssh-key-2020-11-24.key opc@132.145.55.214:/home/opc/Data/coindesk.db /tmp/db_vm1", shell=True)


def load_db_to_df():



if __name__ == "__main__":
    # execute only if run as a script
    sync_dbs()