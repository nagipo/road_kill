import json
def log_in(account,password):
    with open('road_kill/account_data.json','r') as a:
       a_info_d=json.load(fp=a)
       print(a_info_d)
       
       if a_info_d[account]== password:
         print('ok')
       else:
           print('wrong')
       
log_in('bee','b123')
    