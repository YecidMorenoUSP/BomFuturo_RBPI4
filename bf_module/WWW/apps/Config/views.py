try:

    from flask import (Blueprint,
                       render_template,
                       redirect, url_for, session)

    from flask import Flask, request, session, send_file
    import random
    import json
    import datetime
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
        
    mydb = MySQL.connect()
    cur = mydb.cursor()
    cur.callproc("GetSensorReport",(0,))

    json_data=[]
    for sr in cur.stored_results():
        row_headers = sr.column_names;
        for x in sr.fetchall():
            json_data.append(dict(zip(row_headers,x)))
        
    res = json.dumps(json_data,default=lambda obj: obj.isoformat());  
    
    response = make_response(res,200)
    response.mimetype = 'application/json'
    return response