from db_pool.connection import connect,cursor

class ManagerDB:
    def getAllMgr(self):
        query = 'select * from user where is_manager = %s'
        cursor.execute(query,(1,))
        datas = cursor.fetchall()
        return datas