import pandas as pd
import mysql.connector
from pymongo import MongoClient

# MySQL
SQL_HOST = "localhost"
SQL_USER = "root"
SQL_PASSWORD = "Tsabeeh44@" 
SQL_DATABASE = "customers"

# MongoDB
MONGO_URI = "mongodb://localhost:27017/"
MONGO_DATABASE = "Customers"
MONGO_COLLECTION = "customers"
# ---------------------------------------------

EXCEL_FILE = "customers.xlsx" 

def load_excel_data():
    """ Read data from excel file"""
    try:
        df = pd.read_excel(EXCEL_FILE)
        return df.to_dict('records')
    except FileNotFoundError:
        print(f"Error: Excel file '{EXCEL_FILE}' not found.")
        return []
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return []

# === 1 MySQL ===
def setup_mysql(data):
    try:
        conn = mysql.connector.connect(host=SQL_HOST, user=SQL_USER, password=SQL_PASSWORD)
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {SQL_DATABASE}")
        conn.database = SQL_DATABASE
        
        TABLE_SCHEMA = """
        CREATE TABLE IF NOT EXISTS customers (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(255),
            Email VARCHAR(255),
            Product VARCHAR(255),
            Price DECIMAL(10, 2),
            Date DATE
        )
        """
        cursor.execute("DROP TABLE IF EXISTS customers") # create table and remove it
        cursor.execute(TABLE_SCHEMA)
        
        insert_query = """
        INSERT INTO customers (ID,Name, Email, Product, Price, Date) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        
        print("Inserting data into MySQL...")
        for row in data:
             values = (
                row.get('ID'),
                row.get('Name'),
                row.get('Email'),
                row.get('Product'),
                row.get('Price'),
                row.get('Date')
             )
             cursor.execute(insert_query, values)
            
        conn.commit()
        print(f"Successfully loaded {len(data)} records into MySQL.")
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")

# ==2. MongoDB ===
def setup_mongodb(data):
    try:
        client = MongoClient(MONGO_URI)
        db = client[MONGO_DATABASE]
        collection = db[MONGO_COLLECTION]
       
        collection.delete_many({})
        
        if data:
            collection.insert_many(data)
            print(f"Successfully loaded {len(data)} documents into MongoDB.")
        
        client.close()
        
    except Exception as e:
        print(f"MongoDB Error: {e}")

if __name__ == "__main__":
    customer_data = load_excel_data()
    if customer_data:
        setup_mysql(customer_data)
        setup_mongodb(customer_data)