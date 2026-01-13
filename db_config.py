import mysql.connector
import os

def create_connection():

    try:
        return mysql.connector.connect(
            
            host=os.environ.get('MYSQLHOST', 'localhost'),
            user=os.environ.get('MYSQLUSER', 'root'),
            password=os.environ.get('MYSQLPASSWORD', ''), 
            database=os.environ.get('MYSQLDATABASE', 'gym_db'),
            port=int(os.environ.get('MYSQLPORT', 24890))
        )
    except mysql.connector.Error as err:
        print(f"Database Connection Error: {err}")
        return None
