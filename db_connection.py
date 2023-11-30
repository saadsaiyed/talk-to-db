import mysql.connector
from mysql.connector import Error

db = mysql.connector.connect(
    host = "mysql-hackathon-23944e6d-lenicholsdev.a.aivencloud.com",
    user = "avnadmin",
    port = "12715",
    password = "AVNS_y-TKYj1TQtHfx4qSgDj",
    database = "YIAirlinesHelp"
)

def execute_query(query):
    cursor = db.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for x in results:
            print(x)
    except Error as err:
        print(f"Error: '{err}'")