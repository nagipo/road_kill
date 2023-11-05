import json
import flask
from flask import Flask, Request,jsonify
from flask import render_template


app = Flask(__name__,static_folder='static')





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login' ,methods=['post'])
def log_in():
    with open('road_kill/account_data.json','r') as a: #開啟存放帳號資料的json
       a_info_d=json.load(fp=a)
      
       
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
    
    

if __name__=='__main__':
    app.run()