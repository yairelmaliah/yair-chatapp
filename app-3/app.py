from flask import Flask, request, render_template, redirect
from datetime import datetime
import os

dir = "/tmp/flask-chatapp-yair"
try:
  os.mkdir(dir)
except:
  pass

app = Flask(__name__, static_folder="/tmp/flask-chatapp-yair")

@app.route('/')
def home_route():
  return render_template('index.html')

@app.route('/<name>')
def room_route(name):
  return render_template('index.html')

@app.route('/api/chat/<room_name>', methods=['POST', 'GET'])
def create_message(room_name):
  if request.method == 'POST':
    data = dict(request.form)
    time = datetime.now()
    line = f"[{time}] {data['username']}: {data['msg']}"
    
    with open(f'{dir}/room-{room_name}.txt', "a") as f:
      f.write(f"{line}\n")
    
    return "Msg was created succesfully", 200

  else:
    return redirect(f'/chat/{room_name}')

@app.route('/chat/')
@app.route('/chat/<room_name>')
def get_room(room_name=""):
  try:
    if not room_name:
      return app.send_static_file(f"room-general.txt") , 200
    return app.send_static_file(f"room-{room_name}.txt"), 200
  except:
    return "There are no messages in this room"
  
if __name__ == '__main__':
    app.run(port=80, debug=True, host="0.0.0.0")