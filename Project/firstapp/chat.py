from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'quiwojksdfkljaldjkhfl89ww'
socketio = SocketIO(app)

@app.route( '/' )
def index():
    return render_template('./croom.html')

@socketio.on('test')
def handle_my_test(json):
    print('received test: ' + str(json))
    socketio.emit('my response', json)

if __name__ == '__main__':
    socketio.run(app, debug = True)
