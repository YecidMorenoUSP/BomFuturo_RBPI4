try:

    from flask import (Blueprint,
                       render_template,
                       redirect, url_for, session)

    from flask import Flask, request, session, send_file
    import random
    import json
    from time import time
    from random import random
    from flask import Flask, render_template, make_response
    import bf_module.MQTT.common  as MQTT
    import bf_module.MySQL.common as MySQL
    import bf_module.MySQL.sql_cmd as MySQL_CMD


    from datetime import datetime

except Exception as e:
    print("Some modules didnt load {}".format(e))

config_blueprint = Blueprint('Config', __name__)

@config_blueprint.route('/set_sensor', methods=['GET'])
def set_sensor():
    
    accepted_words = {"Ts","client_id"}

    args = request.args
    print(args)

    for name in args.keys():
        if name in accepted_words:
            print(name)
            MQTT.send("Server","config/esp32",name)
        

    response = make_response("OK")
    response.content_type = 'application/json'
    return response

@config_blueprint.route('/get_sensors', methods=['GET'])
def get_nodes():
    print("Get Nodes");
    
    mydb = MySQL.connect()
    cur = mydb.cursor()
    cur.execute(MySQL_CMD.sql_get_sensors)

    row_headers=[x[0] for x in cur.description] #this will extract row headers
    rv = cur.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
      
    res = json.dumps(json_data);  

    response = make_response(res,200)
    response.mimetype = 'application/json'
    return response