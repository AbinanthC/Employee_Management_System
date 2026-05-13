import re

def validate_name(name):
    return name.strip() != ""


def validate_salary(salary):
    try:
        salary = float(salary)

        if salary < 0:
            return False

        return True

    except ValueError:
        return False


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)