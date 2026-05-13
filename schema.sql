CREATE DATABASE company_db;

/c  company_db;

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    department VARCHAR(100),
    salary DECIMAL(10,2) CHECK (salary >= 0),
    email VARCHAR(150) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);