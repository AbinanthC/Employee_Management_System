from psycopg2 import Error
from config.db import get_connection
from services.validator import (
    validate_name,
    validate_email,
    validate_salary,
)

from psycopg2 import Error
from config.db import get_connection

def add_employee(employee_name, department, salary, email):

    connection = get_connection()

    if connection is None:
        return False, "Database connection failed"

    try:
        cursor = connection.cursor()

        employee_name = employee_name.strip()

        if not validate_name(employee_name):
            return False, "Employee name cannot be empty"

        department = department.strip()

        if not validate_salary(salary):
            return False, "Invalid salary"

        email = email.strip()

        if not validate_email(email):
            return False, "Invalid email format"

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

        return True, "Employee added successfully"

    except Error as e:

        if "duplicate key value" in str(e):
            return False, "Email already exists"
        else:
            return False, f"Database Error: {e}"

    finally:
        cursor.close()
        connection.close()

def view_employees():

    connection = get_connection()

    if connection is None:
        return []

    try:
        cursor = connection.cursor()

        query = "SELECT * FROM employees ORDER BY id"

        cursor.execute(query)

        employees = cursor.fetchall()

        return employees

    except Error as e:
        print("Error:", e)
        return []

    finally:
        cursor.close()
        connection.close()

def search_employee(emp_id):
    connection = get_connection()

    if connection is None:
        return

    try:
        cursor = connection.cursor()


        query = "SELECT * FROM employees WHERE id = %s"

        cursor.execute(query, (int(emp_id),))

        employee = cursor.fetchone()

        return employee

    except Error as e:
        print("Error:", e)

    finally:
        cursor.close()
        connection.close()

def update_salary(emp_id, new_salary):

    connection = get_connection()

    if connection is None:
        return False

    try:
        cursor = connection.cursor()

        if not validate_salary(new_salary):
            return False

        query = """
        UPDATE employees
        SET salary = %s
        WHERE id = %s
        """

        cursor.execute(query, (
            float(new_salary),
            emp_id
        ))

        connection.commit()

        return cursor.rowcount > 0

    except Error as e:
        print("Error:", e)
        return False

    finally:
        cursor.close()
        connection.close()

def delete_employee(emp_id):

    connection = get_connection()

    if connection is None:
        return False

    try:
        cursor = connection.cursor()

        query = "DELETE FROM employees WHERE id = %s"

        cursor.execute(query, (emp_id,))

        connection.commit()

        return cursor.rowcount > 0

    except Error as e:
        print("Error:", e)
        return False

    finally:
        cursor.close()
        connection.close()

def search_by_department(department):

    connection = get_connection()

    if connection is None:
        return []

    try:
        cursor = connection.cursor()

        query = """
        SELECT * FROM employees
        WHERE department ILIKE %s
        """
        department=department.strip()
        cursor.execute(query, (f"%{department}%",))

        employees = cursor.fetchall()

        return employees

    except Error as e:
        print("Error:", e)
        return []

    finally:
        cursor.close()
        connection.close()

def sort_by_salary(order):

    connection = get_connection()

    if connection is None:
        return []

    try:
        cursor = connection.cursor()

        if order == "Ascending":
            query = "SELECT * FROM employees ORDER BY salary ASC"
        else:
            query = "SELECT * FROM employees ORDER BY salary DESC"

        cursor.execute(query)

        employees = cursor.fetchall()

        return employees

    except Error as e:
        print("Error:", e)
        return []

    finally:
        cursor.close()
        connection.close()