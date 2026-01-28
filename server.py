from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)


# Route HTTP classique
@app.route("/")
def index():
  return render_template('index.html')


@socketio.on('connect')
def handle_connect():
  print("Un joueur s'est connecté !")

@socketio.on('submit_word')
def onWord_submit(e):
  print(e)
  emit('word_result', e, broadcast=True)

if __name__ == '__main__':
  socketio.run(app, debug=True)