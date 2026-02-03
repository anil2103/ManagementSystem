#module for login & signup for employee and admin

class AdminAuthentication:
    def __init__(self,db,mgr_id,req_db):
        self.db = db
        self.mgr_db = mgr_id
        self.req_db = req_db

class ManagerAuthentication:
    def __init__(self,db,req_db):
        self.mgr_db = db
        self.req_db = req_db
        
    

class EmployeeAuthentication:
    def __init__(self,db):
        self.db = db
        

    def createEmployee(self,e_name,e_email,password):
    
        self.e_name = e_name        
        self.e_email = e_email
        self.password = password
        self.db.createEmp(self.e_name,self.e_email,self.password)

    def empLogin(self,email):
        return self.db.searchEmp(email)