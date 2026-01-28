from services.auth import EmployeeAuthentication
from repositories.employee_repo import EmployeeDB
from validation.email_validator import email_vali
from validation.pass_validator import password_vali
from getpass4 import getpass
from utils.pass_hash import password_hasher,check_password

#This function is for employee repo
emp_db = EmployeeDB()

emp_auth = EmployeeAuthentication(emp_db)

# This function is for signup new employee
def employeeSignup():
    print('Employee Signup')
    name = input('enter your name:')
    email = input('enter your email:')
    if email_vali(email=email) is not None:
        password = getpass('enter your password:')
        if password_vali(password):
            password = password_hasher(password)
            emp_auth.createEmployee(name,email,password)
        else:
            print('''password is not valid
                  password should minimum length of 5
                  password should contain uppercase characters ex: A B C.....
                  password should contain special characters ex: ! @ # $.....
                  password should contain digits ex: 1 2 3.....''')
            employeeSignup()
    else:
        print(''' email id is not valid !!!!!!''')
        employeeSignup()

def employeeLogin():
    print('employee Login')
    email = input('enter your email id:')
    password = getpass('enter your password:')
    hashed_pw = emp_auth.empLogin(email)
    if check_password(password,hashed_pw):
        print('login successful')
    else:
        print('login failed')