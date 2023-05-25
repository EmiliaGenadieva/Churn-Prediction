#create a database from  a csv file
import sqlite3
import pandas
import os
import warnings

def create_database(csv_file : str = "/home/becode/Downloads/Documents/churn_prediction/data/BankChurners.csv", 
                    database_path : str = "/home/becode/Downloads/Documents/churn_prediction/data",
                    database_name : str = "database.db",
                    warn : bool = True) -> None:
    if not os.path.exists(csv_file):
        if warn:
            warnings.warn("The csv file is not found")
        raise FileNotFoundError("The csv file is not found")

    if not os.path.exists(database_path):
        os.mkdir(database_path)
    database = os.path.join(database_path, database_name)
    if os.path.exists(database):
        if warn:
            warnings.warn("The database already exists, it is deleted and recreated")
        os.remove(database)
    conn = sqlite3.connect(database)
    df = pandas.read_csv(csv_file)
    df.to_sql("bank_churners", conn, if_exists="replace", index=False)
    conn.close()
    return None

if __name__ == "__main__":
    create_database()
