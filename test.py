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
mycursor.execute("SELECT account,password_user,email FROM account")
myresult = mycursor.fetchall() 
print(myresult)
data={
  'account':'bee',
  'password':'b123',
  'email':'b@gmail.com'
} 

sql = "INSERT INTO account (account, password_user,email) VALUES (%s, %s,%s)"
val = (data['account'], data['password'],data['email'])
mycursor.execute(sql,val)
mydb.commit()
# for i in myresult:
#   if data['account'] ==i[0]  :
#     print('x')
#     break
#   else:
#     print('ok')
    
  
      
 

 


    