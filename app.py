import json
import flask
import mysql.connector
from flask import Flask,jsonify
from flask import render_template


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
         
        a_info_d=
        data={
           'account':flask.request.form["account"],
           'password':flask.request.form["password"]
        } 
        if data['account'] in a_info_d:
         return(jsonify( 'have_be_exsited'))
        else:
            a_info_d.update({data['account']:data['password']})
            with open ('road_kill/account_data.json','w') as a:
                json.dump(a_info_d,fp=a)
                return(jsonify('ok'))

   elif flask.request.method=='GET':
        
        return render_template('sign_up.html')
        

if __name__=='__main__':
    app.debug = True
    app.run()