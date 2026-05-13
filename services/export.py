from psycopg2 import Error
from config.db import get_connection
import csv


def export_to_csv():
    connection = get_connection()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        query = "SELECT * FROM employees"

        cursor.execute(query)

        employees = cursor.fetchall()

        with open("data/employees.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "ID",
                "Name",
                "Department",
                "Salary",
                "Email",
                "Created At"
            ])

            writer.writerows(employees)

        print("Data exported to employees.csv")

    except Error as e:
        print("Error:", e)

    finally:
        cursor.close()
        connection.close()
