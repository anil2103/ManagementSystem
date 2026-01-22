from services.auth import EmployeeAuthentication
from repositories.employee_repo import EmployeeDB
#This function is for employee repo
emp_db = EmployeeDB()

emp_auth = EmployeeAuthentication(emp_db)

# This function is for signup new employee
def employeeSignup():
    print('Employee Signup')
    name = input('enter your name:')
    email = input('enter your email:')
    password = input('enter your password:')
    emp_auth.createEmployee(name,email,password)

def employeeLogin():
    print('employee Login')
    