from db_pool.connection import connect,cursor

class RequestDB:
    def createRequest(self,mgr_id):
        query = 'insert into mgr_req (req_by) values(%s)'
        values = (mgr_id,)
        cursor.execute(query,values)
        connect.commit()

    def getAllReq(self):
        query = 'select * from mgr_req'
        cursor.execute(query)
        datas = cursor.fetchall()
        return datas

    def deleteReq(self,id):
        query = 'delete from mgr_req where req_is =%s'
        cursor.execute(query,(id),)
        connect.commit()
        print('Request handles successfully!!!')
    
req_db = RequestDB()
req_db.createRequest(7)