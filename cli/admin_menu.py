from getpass4 import getpass
from dotenv import load_dotenv
import os
from services.auth import AdminAuthentication
from repositories.employee_repo import EmployeeDB
from repositories.manager_repo import ManagerDB

emp_db = EmployeeDB()
mgr_db = ManagerDB()
admin_auth = AdminAuthentication(emp_db,mgr_db)

load_dotenv()

def adminWelcome():
    print('welcome back admin')


def adminLogin():
    password = getpass("enter your password:") 
    print(os.getenv('ADMIN_PW'))
    if password == os.getenv('ADMIN_PW'):
        adminWelcome()
        adminMainMenu()
    else:
        print("check password")
        adminLogin()

def managerPromotion():
    id=int(input('Enter the employee id to promote Employee to manager:'))
    data = admin_auth.db.getEmp(id)
    if data[5] == 0:
        if data is not None:
            admin_auth.db.modifyEmptoMgr(id)
            adminMainMenu()
        else:
            print(f'employee with {id} is not present enter id again')
            managerPromotion()
    else:
        print(f'employee with id {id} is already a manager try with some other employee id')
        managerPromotion()

def adminMainMenu():
    choice = int(input('''
________________________________________________________
|press 1 for all employee data                          |
|press 2 for all manager data                           |
|press 3 for assign employee to manager                 |
|press 4 for project to manager                         |
|press 5 for see the manager request for employee       |
|press 6 for assign employee to manager                 |
|press 7 for update the project                         |
|press 8 for logout                                     |
_________________________________________________________
            Enter your choice:'''))

    if choice == 1:
        emp_datas = admin_auth.db.getAllEmp()
        for emp_data in emp_datas:
            print(f'''
_____________________________________
employee id : {emp_data[0]}          |
employee name : {emp_data[1]}        |
employee email : {emp_data[2]}       |
employee manager id : {emp_data[4]}  |
_____________________________________|''')
        adminMainMenu()
    elif choice ==2 :
        mgr_datas = admin_auth.mgr_db.getAllMgr()
        for mgr_data in mgr_datas:
            print(f'''
_____________________________________
manager id : {mgr_data[0]}          |
manager name : {mgr_data[1]}        |
manager email : {mgr_data[2]}       |
manager manager id : {mgr_data[4]}  |
____________________________________|''')
        adminMainMenu()
    elif choice == 3:
        managerPromotion()
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass
    elif choice == 7:
        pass
    elif choice == 8:
        pass
    else:
        print('enter correct option:')
        adminMainMenu()