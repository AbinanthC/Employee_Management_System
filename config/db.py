import psycopg2
from psycopg2 import Error


def get_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="company_db",
            user="postgres",
            password="15nan30du",
            port="5432"
        )

        return connection

    except Error as e:
        print("Database Connection Error:", e)
        return None