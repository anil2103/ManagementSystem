def seeMgrReq(admin_obj):
    datas=admin_obj.req_db.getAllReq()
    emp_datas = admin_obj.db.getEmpwoMgr()
    if datas    :
        for data in datas :
            print(f' request id {data[0]} :manager id with {data[1]} requesting employee for team')
            choice = int(input('''press 1 for assign employee" 
        "press 2 for cancel request
        "press 3 for got to main memu
        
        Enter the option:'''))
            if choice == 1:
                print('Employee without manager')
                for emp_data in emp_datas:
                    print(f'''
employee id:{emp_data[0]}
employee name : {emp_data[1]}''')
                req_id = int(input('Enter request id:'))
                mgr_id = int(input('Enter manager id:'))
                emp_id = int(input('Enter employee id:'))
                admin_obj.db.updateMgr(emp_id,mgr_id)
                admin_obj.db.req_db.deleteReq(req_id)
                print('request handled successfully  ')
                seeMgrReq(admin_obj)
            elif choice ==2 :
                req_id = int(input('Enter request id to reject:'))
                admin_obj.req_db.deleteReq(req_id)
                print('request removed suceessfully')
                seeMgrReq(admin_obj)
            elif choice == 3:
                return 
            else:
                print('invalid option enter correct option')
                seeMgrReq()
        else:
            print('No request')
            return