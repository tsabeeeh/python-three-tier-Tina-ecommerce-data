# Query System Application
A simple web application built with Streamlit and Python to execute queries against MySQL and MongoDB databases. It provides a user interface to select the database type, input the query, and display the results.
 Prerequisites
To run this application locally, you must have the following installed and running:
 * Python 3.x
 * MySQL Server
 * MongoDB Server (running on localhost:27017 by default)
 * The data file customers.xlsx in the same directory as Data_loader.py.
 Setup and Installation
1. Install Dependencies
Install the necessary Python libraries:
pip install streamlit mysql-connector-python pymongo pandas openpyxl

2. Configure and Load Data
 * Security Note: Update the database credentials (SQL_USER, SQL_PASSWORD, MONGO_URI) in both Backend.py and Data_loader.py to match your local setup.
 * Run the Data_loader.py script to:
   * Create and populate the customers database in MySQL.
   * Create and populate the Customers database/customers collection in MongoDB.

python Data_loader.py

Running the Application
Execute the Streamlit application:

streamlit run App.py

The app will open in your default browser (e.g., http://localhost:8501).
Usage:
How to Query
 * Select Database: Use the sidebar radio button to choose either MySQL or MongoDB.
 * Enter Query:
   * MySQL: Enter a valid SQL query (e.g., SELECT Name, Price FROM customers WHERE price > 50;).
   * MongoDB: Enter a valid MQL filter in JSON format (e.g., {"Name":"omar"}).
 * Execute: Click the "Execute Query" button to see the results.
File Overview
 * App.py: Streamlit front-end and UI logic.
 * Backend.py: Handles database connections and query execution for MySQL and MongoDB.
 * Data_loader.py: Script for initial database setup and data loading from Excel.
   
