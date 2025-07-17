import mysql.connector
import os

DB_CONFIG = {
    "host": "flask-mysql",  # Use MySQL container name
    "user": "root",
    "port": 3306,
    "password": "password",
    "database": "flask_db"
}



# DB_CONFIG = {
#     "host": os.getenv("MYSQL_HOST", "mysql-service"),  # MySQL Service name in K8s
#     "port": int(os.getenv("MYSQL_PORT")),
#     "user": os.getenv("MYSQL_USER"),
#     "password": os.getenv("MYSQL_ROOT_PASSWORD"),
#     "database": os.getenv("MYSQL_DB")
# }



def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)


def create_database_and_table():
    try:
        conn = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            port=DB_CONFIG["port"],
            password=DB_CONFIG["password"]
        )
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS flask_db")
        cursor.close()
        conn.close()

        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users_detail (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL UNIQUE,
                detail VARCHAR(100) NOT NULL
            )
        """)
        cursor.close()
        conn.close()
        print("Database and table checked/created successfully.")
    except mysql.connector.Error as err:
        # print(f"Error: {err}")
        print("Waiting for MySQL...")
        time.sleep(2)

create_database_and_table()

def get_db_connection():
    """Get a connection to the database."""
    return mysql.connector.connect(**DB_CONFIG)
