from cli.employee_menu import employeeSignup,employeeLogin
from cli.admin_menu import adminLogin
from repositories.employee_repo import EmployeeDB

emp_db = EmployeeDB()

def menu():
    while True:
        print('''welcome
              press 1 for admin login
              press 2 for employee signup
              press 3 for employee login''')
        choice=int(input('Enter your option:'))
        if choice ==1:
            adminLogin()
        elif choice == 2:
            employeeSignup()
        elif choice ==3 :
            employeeLogin()
        else:
            print('enter a valid number:')