try:
    
    from flask import render_template

    from flask import (Blueprint,
                       render_template,
                       redirect, url_for)

    from flask import (Flask,
                       request,
                       redirect,
                       session,
                       send_file)

    from io import BytesIO
    from flask import abort, jsonify
    import io
    from  random import sample

    from apps.config import config_dict
    from apps import create_app
    
    from flask_socketio import SocketIO
    from flask_socketio import send, emit

    import os
    import time

    from apps.io_server.routes import create_socket
    

except Exception as e:
    print("Failed to load some Modules ")

# WARNING: Don't run with debug turned on in production!
DEBUG = (os.getenv('DEBUG', 'False') == 'True')

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:
    app_config = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)
socketio = create_socket(app)

# @socketio.on('message')
# def handle_message(data):
#     print('received message: ' + str(data))

# @socketio.on('event_sync')
# def handle_time():
#     emit('event_sync',"Hola sync")

# @socketio.on('get_sensor_data')
# def handle_get_sensor_data(data):
#     if(data == 0):
#         emit('get_sensor_data',"First Res0")
#     else:
#         emit('get_sensor_data',f"Res{data}")

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
    print("END")
    None
