import mysql.connector

def create_connection():
    try:
        conn = mysql.connector.connect(
            host="mainline.proxy.rlwy.net",
            user="root",
            password="YhrBFaJsFeguphapTEzOEnoquzRozFBX",
            database="railway",
            port=14890,
            connection_timeout=60
        )
        return conn
    except Exception as e:
        print(f"Connection Error: {e}")
        return None
