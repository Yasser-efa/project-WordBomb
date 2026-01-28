from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

users = {}

@socketio.on('set_username')
def username_handler(data):
  username = data.get('username', 'Anonyme')
  users[request.sid] = username
  print(f"{username} ({request.sid}) s'est identifié")


# Route HTTP classique
@app.route("/")
def index():
  return render_template('index.html')


@socketio.on('connect')
def handle_connect():
  print("Un joueur s'est connecté !")

@socketio.on('submit_word')
def onWord_submit(e):
  emit('word_result', f'{users[request.sid]} a écrit: {e.get('word')}', broadcast=True)

if __name__ == '__main__':
  socketio.run(app, debug=True)