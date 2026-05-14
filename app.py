import streamlit as st
import pandas as pd
import base64
from services.export import export_to_csv
from services.employee import(
    add_employee,
    view_employees,
    sort_by_salary,
    delete_employee,
    search_by_department,
    update_salary,
    search_employee,
)

def get_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_image = get_base64("assets/bg.png")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(
    page_title="Employee_Management_System",
    page_icon="assets/office.png",
    layout='wide'
)

st.markdown(
    "<h1 style='color:black;'>Employee Management System</h1>",
    unsafe_allow_html=True
)

choice = st.sidebar.selectbox(
    "MENU",
    [
        "Add Employee",
        "View Employee",
        "Search Employee",
        "Update Salary",
        "Delete Employee",
        "Sort Employee",
        "Search Dept",
        "Export to CSV"
    ]
)

if choice == "Add Employee":
    st.subheader("Add new Employee")
    employee_name = st.text_input("Employee Name")
    department = st.text_input("Department")
    salary = st.number_input("Salary", min_value=0.0)
    email = st.text_input("Email")

    if st.button("Add Employee"):
        success, message=add_employee(
            employee_name,
            department,
            salary,
            email
        )
        if success:
            st.success(message)
        else:
            st.error(message)

elif choice == "View Employee":

    st.subheader("Employee Records")

    employees = view_employees()
    if employees:

        df = pd.DataFrame(employees, columns=[
            "ID",
            "Name",
            "Department",
            "Salary",
            "Email",
            "Created At"
        ])

        st.dataframe(df, use_container_width=True)

    else:
        st.warning("No employees found")

elif choice == "Search Employee":

    st.subheader("Search Employee")

    emp_id = st.number_input("Enter Employee ID", min_value=1)

    if st.button("Search"):

        employee = search_employee(emp_id)

        if employee:
            st.success("Employee Found")

            st.write(f"ID: {employee[0]}")
            st.write(f"Name: {employee[1]}")
            st.write(f"Department: {employee[2]}")
            st.write(f"Salary: {employee[3]}")
            st.write(f"Email: {employee[4]}")
            st.write(f"Created At: {employee[5]}")

        else:
            st.error("Employee not found")

elif choice == "Update Salary":

    st.subheader("Update Employee Salary")

    emp_id = st.number_input("Employee ID", min_value=1)
    new_salary = st.number_input("New Salary", min_value=0.0)

    if st.button("Update Salary"):

        updated = update_salary(emp_id, new_salary)

        if updated:
            st.success("Salary updated successfully")
        else:
            st.error("Employee not found")      


elif choice == "Delete Employee":

    st.subheader("Delete Employee")

    emp_id = st.number_input("Employee ID", min_value=1)

    if st.button("Delete Employee"):

        deleted = delete_employee(emp_id)

        if deleted:
            st.success("Employee deleted successfully")
        else:
            st.error("Employee not found")      

elif choice == "Search Dept":

    st.subheader("Search Employee by Dep.")

    department = st.text_input("Enter Department Name")

    if st.button("Search"):

        employee = search_by_department(department)

        if employee:
            for emp in employee:
                st.write(f"ID: {emp[0]}")
                st.write(f"Name: {emp[1]}")
                st.write(f"Department: {emp[2]}")
                st.write(f"Salary: {emp[3]}")
                st.write(f"Email: {emp[4]}")
                st.write(f"Created At: {emp[5]}")

        else:
            st.error("Employee not found")


elif choice == "Sort Employee":

    st.subheader(" Sort Employees By Salary")

    sort_order = st.radio(
        "Select Order",
        ["Ascending", "Descending"]
    )

    if st.button("Sort"):

        data = sort_by_salary(sort_order)

        if data:

            columns = [
                "ID",
                "Employee Name",
                "Age",
                "Department",
                "Email",
                "Salary"
            ]

            df = pd.DataFrame(data, columns=columns)

            st.dataframe(df, use_container_width=True)

        else:
            st.warning("No Employees Found")



elif choice == "Export to CSV":

    st.subheader("📁 Export Employee Data")

    if st.button("Export CSV"):

        export_to_csv()

        with open("data/employees.csv", "rb") as file:

            st.download_button(
                label="⬇ Download CSV",
                data=file,
                file_name="employees.csv",
                mime="text/csv"
            )

        st.success("CSV Exported Successfully")
