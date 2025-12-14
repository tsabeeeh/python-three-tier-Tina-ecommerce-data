import mysql.connector
from pymongo import MongoClient
import json
from bson.json_util import dumps 

SQL_HOST = "localhost"
SQL_USER = "root"
SQL_PASSWORD = "Tsabeeh44@" 
SQL_DATABASE = "customers"

MONGO_URI = "mongodb://localhost:27017/"
MONGO_DATABASE = "Customers"
MONGO_COLLECTION = "customers"
# ---------------------------------------------

def execute_sql_query(query: str):
    """Execution an SQL query on MySQL"""
    result = "N/A"
    try:
        conn = mysql.connector.connect(
            host=SQL_HOST, 
            user=SQL_USER, 
            password=SQL_PASSWORD , 
            database=SQL_DATABASE
        )
        cursor = conn.cursor()
        
        #Execute Query
        cursor.execute(query)
        
        # get results
        if query.strip().upper().startswith("SELECT"):
            columns = [i[0] for i in cursor.description]
            data = cursor.fetchall()
            results_list = [dict(zip(columns, row)) for row in data]
            result = json.dumps(results_list, indent=2, default=str)
        else:
      # UPDATE/DELETE/INSERT in Query
            conn.commit()
            result = f"Command executed successfully. Rows affected: {cursor.rowcount}"

        cursor.close()
        conn.close()
        return result
        
    except mysql.connector.Error as err:
        return f"SQL Error: {err}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def execute_mongodb_query(query_str: str):
    """ Executes a MongeBD query (MQL) using find on 'customers_collec'"""
    try:
        client = MongoClient(MONGO_URI)
        db = client[MONGO_DATABASE]
        collection = db[MONGO_COLLECTION]
        
        query_filter = json.loads(query_str)
        
        mongo_results = collection.find(query_filter)
        
        result = dumps(list(mongo_results), indent=2)
        
        client.close()
        return result
        
    except json.JSONDecodeError:
        return "MongoDB Query Error: Invalid JSON format for the query."
    except Exception as e:
        return f"MongoDB Error: {e}"

def process_request(db_type: str, query: str):
    """ Main function that call the correct execution function """
    if not query.strip():
        return "Error: Query cannot be empty."
        
    if db_type.lower() == 'mysql':
        return execute_sql_query(query)
    elif db_type.lower() == 'mongodb':
        return execute_mongodb_query(query)
    else:
        return "Error: Invalid database type selected."