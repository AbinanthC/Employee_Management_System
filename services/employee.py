from psycopg2 import Error
from config.db import get_connection
from services.validator import (
    validate_name,
    validate_email,
    validate_salary,
)

def add_employee():
    connection = get_connection()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        employee_name = input("Enter Employee Name: ").strip()

        if not validate_name(employee_name):
            print("Employee name cannot be empty.")
            return

        department = input("Enter Department: ").strip()

        salary = input("Enter Salary: ")

        if not validate_salary(salary):
            print("Invalid salary.")
            return

        email = input("Enter Email: ").strip()

        if not validate_email(email):
            print("Invalid email format.")
            return

        query = """
        INSERT INTO employees (employee_name, department, salary, email)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(query, (
            employee_name,
            department,
            float(salary),
            email
        ))

        connection.commit()

        print("Employee added successfully.")

    except Error as e:

        if "duplicate key value" in str(e):
            print("Email already exists.")
        else:
            print("Database Error:", e)

    finally:
        cursor.close()
        connection.close()

def view_employees():
    connection = get_connection()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        query = "SELECT * FROM employees ORDER BY id"

        cursor.execute(query)

        employees = cursor.fetchall()

        if not employees:
            print("No employees found.")
            return

        print("\n----- Employee Records -----")

        for emp in employees:
            print(f"""
ID: {emp[0]}
Name: {emp[1]}
Department: {emp[2]}
Salary: {emp[3]}
Email: {emp[4]}
Created At: {emp[5]}
-----------------------------
""")

    except Error as e:
        print("Error:", e)

    finally:
        cursor.close()
        connection.close()

def search_employee():
    connection = get_connection()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        emp_id = input("Enter Employee ID: ")

        if not emp_id.isdigit():
            print("Invalid ID.")
            return

        query = "SELECT * FROM employees WHERE id = %s"

        cursor.execute(query, (int(emp_id),))

        employee = cursor.fetchone()

        if employee:
            print(f"""
ID: {employee[0]}
Name: {employee[1]}
Department: {employee[2]}
Salary: {employee[3]}
Email: {employee[4]}
Created At: {employee[5]}
""")
        else:
            print("Employee not found.")

    except Error as e:
        print("Error:", e)

    finally:
        cursor.close()
        connection.close()

def update_salary():
    connection = get_connection()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        emp_id = input("Enter Employee ID: ")

        if not emp_id.isdigit():
            print("Invalid ID.")
            return

        new_salary = input("Enter New Salary: ")

        if not validate_salary(new_salary):
            print("Invalid salary.")
            return

        query = """
        UPDATE employees
        SET salary = %s
        WHERE id = %s
        """

        cursor.execute(query, (
            float(new_salary),
            int(emp_id)
        ))

        connection.commit()

        if cursor.rowcount == 0:
            print("Employee not found.")
        else:
            print("Salary updated successfully.")

    except Error as e:
        print("Error:", e)

    finally:
        cursor.close()
        connection.close()

def delete_employee():
    connection = get_connection()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        emp_id = input("Enter Employee ID: ")

        if not emp_id.isdigit():
            print("Invalid ID.")
            return

        query = "DELETE FROM employees WHERE id = %s"

        cursor.execute(query, (int(emp_id),))

        connection.commit()

        if cursor.rowcount == 0:
            print("Employee not found.")
        else:
            print("Employee deleted successfully.")

    except Error as e:
        print("Error:", e)

    finally:
        cursor.close()
        connection.close()

def search_by_department():
    connection = get_connection()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        department = input("Enter Department Name: ")

        query = """
        SELECT * FROM employees
        WHERE department ILIKE %s
        """

        cursor.execute(query, (department,))

        employees = cursor.fetchall()

        if employees:
            for emp in employees:
                print(f"""
                      ID: {emp[0]}
                      Name: {emp[1]}
                      Department: {emp[2]}
                      Salary: {emp[3]}
                      Email: {emp[4]}
                      Created At: {emp[5]}
                      -----------------------------
                      """)
        else:
            print("No employees found.")

    except Error as e:
        print("Error:", e)

    finally:
        cursor.close()
        connection.close()

def sort_by_salary():
    connection = get_connection()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        query = """
        SELECT * FROM employees
        ORDER BY salary DESC
        """

        cursor.execute(query)

        employees = cursor.fetchall()

        for emp in employees:
            print(f"""
                      ID: {emp[0]}
                      Name: {emp[1]}
                      Department: {emp[2]}
                      Salary: {emp[3]}
                      Email: {emp[4]}
                      Created At: {emp[5]}
                      -----------------------------
                      """)

    except Error as e:
        print("Error:", e)

    finally:
        cursor.close()
        connection.close()

