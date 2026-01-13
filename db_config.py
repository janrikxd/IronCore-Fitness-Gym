import mysql.connector
import os

def create_connection():
    try:
        return mysql.connector.connect(
            host=os.environ.get('MYSQLHOST'),
            user=os.environ.get('MYSQLUSER'),
            password=os.environ.get('MYSQLPASSWORD'),
            database=os.environ.get('MYSQLDATABASE'),
            port=int(os.environ.get('MYSQLPORT'))
        )
    except Exception as err:
        print(f"Error: {err}")
        return None
