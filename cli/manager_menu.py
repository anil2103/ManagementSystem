from repositories import request_repo,manager_repo
from services import manager_services
from services.auth import ManagerAuthentication

mgr_db = manager_repo.ManagerDB()
req_db = request_repo.RequestDB()
mgr_auth = ManagerAuthentication(mgr_db,req_db)

def managerWelcome(mgr_id):
    print(f'Welcome {mgr_id}')

def managerMainMenu(mgr_id):
    managerWelcome(mgr_id=mgr_id)
    choice = int(input('''
press 1 for view your team
press 2 for view project assigned by admin
press 3 for give task for employee
press 4 for manager request employee for the team
press 5 for manager verify the task 
enter your choice:'''))
    if choice == 1:
        manager_services.viewAllEmp(mgr_id,mgr_auth)
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        manager_services.mgrRequest(mgr_auth,mgr_id)
        managerMainMenu(mgr_id)
    elif choice == 5:
        pass
    req_db