import json
import  mysql.connector
def log_in(account,password):
    with open('road_kill/account_data.json','r') as a:
       a_info_d=json.load(fp=a)
       print(a_info_d)
       
       if a_info_d[account]== password:
         print('ok')
       else:
           print('wrong')
           
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="lab_wild"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SELECT account,password_user FROM account")
myresult = mycursor.fetchall() 
print(myresult)  
a_info_d=dict()
for i in myresult:
  a_info_d[i[0]]=i[1]  
  
      
print(a_info_d)  

 


    