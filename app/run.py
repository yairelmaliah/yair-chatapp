from flask import request, render_template, redirect
from db import mysql
from app import app
import pymysql
from datetime import datetime
import socket

# Get container IP
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)  

# General room
@app.route('/')
def general_room_route():
  return render_template('index.html', ip=IPAddr)

# Any room
@app.route('/<name>')
def room_route(name):
  return render_template('index.html', ip=IPAddr)

# Chat room
@app.route('/api/chat/<room_name>', methods=['POST', 'GET'])
def create_message(room_name):
  if request.method == 'POST':
    
    # Extract message data 
    data = dict(request.form)
    data['room_name'] = room_name
    data['time'] = datetime.now()

    # Insert room message to db
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = "INSERT INTO `rooms` (`room_name`, `username`, `msg`, `msg_date`) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (room_name, data['username'], data['msg'], data['time']))
    conn.commit()

    return {"msg":"success", "status_code": 200}, 200

  # For getting all messages redirect
  if request.method == 'GET':
    return redirect(f'/chat/{room_name}')


@app.route('/chat/')
@app.route('/chat/<room_name>')
def get_room(room_name=""):
  
  if not room_name:
    room_name = "general"
  
  # Fetch room messages
  conn = mysql.connect()
  cursor = conn.cursor(pymysql.cursors.DictCursor)
  sql = "SELECT * FROM rooms WHERE room_name=%s"
  cursor.execute(sql, (room_name,))
  res = cursor.fetchall()

  # Get numbers of romm messages
  res_len = len(list(res))

  if not res:
    return "There are no messages in this room :("

  return render_template("messages.txt", results=res, res_len=res_len), 200


if __name__ == '__main__':
    app.run(port=80, debug=True, host="0.0.0.0")