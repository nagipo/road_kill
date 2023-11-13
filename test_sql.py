import random
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="lab_wild"
)
mycursor = mydb.cursor()
# data={'account_id':'bee'}
# search="SELECT account_id FROM `account` WHERE account='"+data['account_id']+"'"
# mycursor.execute(search)
# myresult = mycursor.fetchall()
# print(myresult[0][0])
search="SELECT upload_id,identifi,location FROM `upload` WHERE challenge is null"
mycursor.execute(search)
myresult = mycursor.fetchall()
res=[]
if len(myresult)<=5:
    
    for i in range(len(myresult)):
      res.append({
        'upload_id':myresult[i-1][0],
        'identifi':myresult[i-1][1],
        'location':myresult[i-1][2]
        })
else:
    re_sample= random.sample(myresult,k=5)
    for i in range(len(re_sample)):
      res.append({
        'upload_id':re_sample[i-1][0],
        'identifi':re_sample[i-1][1],
        'location':re_sample[i-1][2]
        })
    print(res)