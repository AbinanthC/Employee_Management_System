from services.employee import(
    add_employee,
    view_employees,
    search_employee,
    update_salary,
    delete_employee,
    search_by_department,
    sort_by_salary,
)
from services.export import export_to_csv
from psycopg2 import Error

def main():

    while True:

        print("""
======== Employee Management System ========

1. Add Employee
2. View Employees
3. Search Employee
4. Update Salary
5. Delete Employee
6. Search by Department
7. Sort Employees by Salary
8. Export to CSV
9. Exit

============================================
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_salary()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            search_by_department()

        elif choice == "7":
            sort_by_salary()

        elif choice == "8":
            export_to_csv()

        elif choice == "9":
            print("Exiting application...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()