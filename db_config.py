import mysql.connector
import os

def create_connection():
    try:
        conn = mysql.connector.connect(
            host="mainline.proxy.rlwy.net",
            user="root",
            password="YhrBFaJsFeguphapTEzOEnoquzRozFBX",
            database="railway",
            port=14890,
            
            connect_timeout=10 
        )
        if conn.is_connected():
            print("Successfully connected to Railway Database!")
            return conn
            
    except mysql.connector.Error as err:
       
        print(f"Database Error: {err}")
        return None
    except Exception as e:
        print(f"General Error: {e}")
        return None

