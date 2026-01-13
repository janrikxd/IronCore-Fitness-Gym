import mysql.connector
import os

def create_connection():
    try:

        host = os.environ.get('MYSQLHOST', 'localhost')
        user = os.environ.get('MYSQLUSER', 'root')
        password = os.environ.get('MYSQLPASSWORD', '')
        database = os.environ.get('MYSQLDATABASE', 'gym_db')
        port = int(os.environ.get('MYSQLPORT', 3306))

        return mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
