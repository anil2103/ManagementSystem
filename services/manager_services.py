def viewAllEmp(mgr_id,mgr_obj):
    datas = mgr_obj.mgr_db.getEmp(mgr_id)
    if datas:
        print('YOUR TEAM:')
        for data in datas:
            print(f'''
employee id : {data[0]}
employee name : {data[1]}
employee email : {data[2]}''')
    else:
        print('No Employee Assigned Yet')
        mgrOption(mgr_id,mgr_obj)

def mgrRequest(mgr_obj,mgr_id):
    input = input('press enter to request a employee for a team')
    mgr_obj.req_db.createRequest(mgr_id)
    print('request sent to admin successfully')
def mgrOption(mgr_id,mgr_obj):
        print('''enter 1 for request employee from admin
            enter 2 for go back to main menu''')
        choice = int(input('Enter your option:'))
        if choice == 1:
            mgrRequest(mgr_obj,mgr_id)
        elif choice == 2:
            return
        else:
             print('Invalid choice ')