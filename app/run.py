from flask import request, render_template, redirect, jsonify
from db import mysql
import pymysql
from app import app
from datetime import datetime
import socket   
import os

hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)  

dir = "/tmp/flask-chatapp-yair"
try:
  os.mkdir(dir)
except:
  pass




@app.route('/')
def home_route():
  return render_template('index.html', ip=IPAddr)


@app.route('/<name>')
def room_route(name):
  return render_template('index.html', ip=IPAddr)

@app.route('/api/chat/<room_name>', methods=['POST', 'GET'])
def create_message(room_name):
  if request.method == 'POST':

    data = dict(request.form)

    data['room_name'] = room_name
    data['time'] = datetime.now()

    print(data, flush=True)

    sql = "INSERT INTO `rooms` (`room_name`, `username`, `msg`, `msg_date`) VALUES (%s, %s, %s, %s)"
    conn = mysql.connect()
    
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    cursor.execute(sql, (room_name, data['username'], data['msg'], data['time']))

    conn.commit()

    return {"msg":"success", "status_code": 200}, 200

  if request.method == 'GET':
    return redirect(f'/chat/{room_name}')


@app.route('/chat/')
@app.route('/chat/<room_name>')
def get_room(room_name=""):
  
  if not room_name:
    room_name = "global"
  
  conn = mysql.connect()
  cursor = conn.cursor(pymysql.cursors.DictCursor)
  sql = "SELECT * FROM rooms WHERE room_name=%s"
  cursor.execute(sql, (room_name,))

  res = cursor.fetchall()
  
  res_len = len(list(res))

  if not res:
    return "There are no messages in this room :("

  return render_template("messages.txt", results=res, res_len=res_len), 200


if __name__ == '__main__':
    app.run(port=80, debug=True, host="0.0.0.0")