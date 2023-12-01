import mysql.connector, os
from mysql.connector import Error

# This is to import all the environment variables
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv('config/.env'))

db = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USERNAME"),
    port = os.getenv("DB_PORT"),
    password = os.getenv("DB_PASSWORD"),
    database = os.getenv("DB_DATABASE")
)

def execute_query(query):
    cursor = db.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for x in results:
            print(x)
        return results
    except Error as err:
        print(f"Error: '{err}'")