from db_pool.connection import connect,cursor

class ManagerDB:
    def getAllMgr(self):
        query = 'select * from user where is_manager = %s'
        cursor.execute(query,(1,))
        datas = cursor.fetchall()
        return datas
    def getEmp(self,id):
        query = 'select * from user where mgr_id = %s'
        cursor.execute(query)
        datas = cursor.fetchall()
        return datas