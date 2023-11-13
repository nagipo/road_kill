import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="lab_wild"
)
mycursor = mydb.cursor()

with open('test.jpg','rb') as f:
    image = f.read()
    
sql="INSERT INTO upload(upload_img,account_id,identifi) VALUES(%s,1,'Muntiacus reevesi')"
val=[image]


mycursor.execute(sql,val)
mydb.commit()