from db_pool.connection import connect,cursor

class EmployeeDB:
    def createEmp(self,name,email,password):
        query = 'insert into user(user_name,user_email,password) value (%s,%s,%s)'
        values = (name,email,password)
        cursor.execute(query,values)
        connect.commit()
        print('user created successfully!!!')

    def searchEmp(self,email):
        query = 'select * from user where user_email = %s'
        values = email,
        cursor.execute(query,values)
        data = cursor.fetchone()
        if data is not None:
            return data
        else:
            return
        
    def getEmp(self,id):
        query = 'select * from user where user_id = %s'
        cursor.execute(query,(id,))
        datas = cursor.fetchone()
        return datas

    def getAllEmp(self):
        query = 'select * from user where is_employee =%s and is_manager=%s '
        cursor.execute(query,(1,0))
        datas = cursor.fetchall()
        return datas
    def modifyEmptoMgr(self,id):
        query = 'update user set is_manager = %s where user_id = %s'
        values = (1,id)
        cursor.execute(query,values)
        connect.commit()
        print(f'employee id with {id} promoted to manager.')

    def getEmpwoMgr(self):
        query = 'select * from user where is_employee = 1 and is_manager = 0 and mgr_id is null'
        
        cursor.execute(query,)
        datas = cursor.fetchall()
        return datas
    def updateMgr(self,emp_id,mgr_id):
        query = 'update user set mgr_id = %s where user_id = %s'
        values = (mgr_id,emp_id)
        cursor.execute(query,values)
        connect.commit()
        print(f'employee id with {emp_id} got assigned to manager id {mgr_id}')
