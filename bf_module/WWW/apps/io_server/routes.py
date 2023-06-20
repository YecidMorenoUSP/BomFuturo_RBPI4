from flask_socketio import SocketIO
from flask_socketio import send, emit

def create_socket(app):
    socketio = SocketIO(app)
    configureSocket(socketio)
    return socketio


def configureSocket(socketio):
    @socketio.on('message')
    def handle_message(data):
        print('received message: ' + str(data))

    @socketio.on('event_sync')
    def handle_time():
        emit('event_sync',"Hola sync")

    @socketio.on('get_sensor_data')
    def handle_get_sensor_data(data):
        if(data == 0):
            emit('get_sensor_data',"First Res0")
        else:
            emit('get_sensor_data',f"Res{data}")