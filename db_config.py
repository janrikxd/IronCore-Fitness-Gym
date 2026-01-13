import mysql.connector

def create_connection():
    try:
        return mysql.connector.connect(
            host="tramway.proxy.rlwy.net",
            user="root",
            password="jlLxhTwMbOKTooHQzEBBgpgtwqTIXZWg",
            database="railway",
            port=14890
        )
    except Exception as err:
        print(f"Error: {err}")
        return None
