import random
import flask
import mysql.connector
from flask import Flask,jsonify,render_template
import smtplib
smtp=smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login('ericpo2206@gmail.com','opwu kkin yfvf hspg')


app = Flask(__name__,static_folder='static')


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="lab_wild"
)
mycursor = mydb.cursor()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login' ,methods=['post'])
def log_in():
    # with open('road_kill/account_data.json','r') as a: #開啟存放帳號資料的json
    #    a_info_d=json.load(fp=a)
      
    mycursor.execute("SELECT account,password_user FROM account")
    myresult = mycursor.fetchall() 
    
    a_info_d={} 
    for i in myresult:
      a_info_d[i[0]]=i[1]
        
    
    data={
           'account':flask.request.form["account"],
           'password':flask.request.form["password"]
       } #從client端取得使用者輸入之帳密
       
       
    if data['account'] in a_info_d:
           if a_info_d[data['account']]== data['password']:
             return(jsonify( 'ok'))
           else:
             return(jsonify('password_wrong'))
           
    else:
         return(jsonify( 'account_wrong')) #判斷帳密是否正確
    
@app.route('/sign_up',methods=['get','post'])  
def sign_up(): 
   if flask.request.method=='POST':
         
        mycursor.execute("SELECT account,password_user FROM account")
        myresult = mycursor.fetchall() 
    
        a_info_d={} 
        for i in myresult:
          a_info_d[i[0]]=i[1]
        data={
           'account':flask.request.form["account"],
           'email':flask.request.form["email"]
        } 
        
        for i in myresult:
            if data['account'] ==i[0]  :
                return(jsonify( 'have_be_exsited'))
                
            else:
                sql = "INSERT INTO account (account, password_user,email) VALUES (%s, %s,%s)"
                val = (data['account'], data['password'],data['email'])
                mycursor.execute(sql,val)
                mydb.commit()
                
                return(jsonify( 'ok'))
                
        

   elif flask.request.method=='GET':
        
        return render_template('sign_up.html')
        
@app.route('/forget_password',methods=['get','post']) 
def forget_password():
    if flask.request.method=='GET':
        return render_template('forget_password.html')
    elif flask.request.method=='POST':
        data={
           'account':flask.request.form["account"],
           'email':flask.request.form["email"]
        }
        print(data)
        new_password=str(random.randint(1000,9999))
        from_addr='ericpo2206@gmail.com'
        to_addr=data['email']
        msg=f"Subject:your ne password\n{new_password}"
        status=smtp.sendmail(from_addr, to_addr, msg)#加密文件，避免私密信息被截取
        if status=={}:
            print("郵件傳送成功!")
        else:
            print("郵件傳送失敗!")
        smtp.quit()
        sql="UPDATE account SET password_user='"+new_password+"'WHERE account='"+data["account"]+"'"
        print(sql)
        mycursor.execute(sql)
        mydb.commit()
        return jsonify( 'ok')
        # UPDATE account SET email='a@hotmail.com' WHERE account='apple'
        
@app.route('/upload',methods=['get','post'])
def upload():
  if  flask.request.method=='GET': 
      return render_template('upload.html')
  elif flask.request.method=='POST':
     data={
           'file':flask.request.files['file'],
           'account_id':flask.request.form['account_id'],
           'sp_name':flask.request.form["sp_name"],
           'time':flask.request.form["time"],
           'locationlocation':flask.request.form["location"]
           
        }
    #  file=flask.request.files['file']
    #  print(data)
     search="SELECT account_id FROM `account` WHERE account='"+data['account_id']+"'"
     mycursor.execute(search)
     myresult = mycursor.fetchall()
    #  print(myresult)
     
     sql='INSERT INTO upload( `upload_img`, `account_id`, `identifi`,  `location`) VALUES (%s,%s,%s,%s)'  
     val= (data['file'].read(),myresult[0][0],data['sp_name'],data['locationlocation'])  
     mycursor.execute(sql,val)
     mydb.commit()
     return jsonify( 'ok')
   
   
@app.route('/identi',methods=['get','post'])   
def identi():
  if flask.request.method=='GET':
    return render_template('identi.html')
  elif flask.request.method=='POST':
    return
  
@app.route('/identi/table',methods=['get']) 
def identi_table():
  search="SELECT upload_id,identifi,location FROM `upload` WHERE challenge is null"
  mycursor.execute(search)
  myresult = mycursor.fetchall()
  if len(myresult)<=5:
    res=[]
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
  return jsonify(res)
  
  

if __name__=='__main__':
    app.debug = True
    app.config['MAX_CONTENT_LENGTH']=100*1024*1024
    app.run()