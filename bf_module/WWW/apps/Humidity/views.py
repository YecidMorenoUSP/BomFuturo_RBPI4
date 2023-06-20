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
    import bf_module.MySQL.common as MySQL
    import bf_module.MySQL.sql_cmd as MySQL_CMD
    from datetime import datetime

except Exception as e:
    print("Some modules didnt load {}".format(e))

humidity_blueprint = Blueprint('Humidity', __name__)


@humidity_blueprint.route('/humidity', methods=['GET'])
def humidity():
    
    required_keys = {"topic","from"}

    args = request.args

    data = {}

    if required_keys.issubset(args.keys()) :  

        mydb = MySQL.connect()
        mycursor = mydb.cursor()

        mycursor.callproc("GetLastSensorDataByTopic",(args["topic"],args["from"]));
        data["values"] = []
        data["from"] = args["from"]
        for sr in mycursor.stored_results():
            colum_names = sr.column_names
            res = sr.fetchall()
            if(res):
                for x in res:
                    d = dict(zip(colum_names,x))
                    data["values"].append([d["time_ts"].timestamp(), d['value']])
                data["from"] = d["hr_id"]


    response = make_response(json.dumps(data,
                    default=lambda obj: obj.isoformat()))
    response.content_type = 'application/json'
    return response
