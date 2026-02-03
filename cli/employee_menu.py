from services.auth import EmployeeAuthentication
from repositories.employee_repo import EmployeeDB
from validation.email_validator import email_vali
from validation.pass_validator import password_vali
from getpass4 import getpass
from utils.pass_hash import password_hasher,check_password
from .manager_menu import managerMainMenu

#This function is for employee repo
emp_db = EmployeeDB()

emp_auth = EmployeeAuthentication(emp_db)

# This function is for signup new employee
def employeeSignup():
    print('Employee Signup')
    name = input('enter your name:')
    email = input('enter your email:')
    verify_email = emp_db.searchEmp(email)
    if verify_email is None:
        if email_vali(email=email) is not None:
            password = getpass('enter your password:')
            confirm_pw =getpass('enter your password again:')
            if password == confirm_pw:
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
                print('password and confirm_pw both are not same')
                employeeSignup()        
        else:
            print(''' email id is not valid !!!!!!''')
            employeeSignup()
    else:
        print(f'account with thisemail id {email} is already exist.login')
        employeeLogin
def employeeLogin():
    print('employee Login')
    email = input('enter your email id:')
    password = getpass('enter your password:')
    data = emp_auth.empLogin(email)
    hashed_pw = data[3]
    is_manager = data[5]
    if check_password(password,hashed_pw):
        if is_manager == 1:
            print('manager login successfull !!!')
            managerMainMenu(data[0])
        else:
            print('employee login successfull')
    else:
        print('login failed')