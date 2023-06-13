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
    
    args = request.args
    print(args["from"])

    mydb = MySQL.connect()

    mycursor = mydb.cursor()
    # mycursor.execute("SELECT date,value FROM humidity_reads;")
    if(args["from"] == "NaN"):
        mycursor.execute(MySQL_CMD.sql_last_values)
    else:
        mycursor.execute(MySQL_CMD.sql_last_values_from%(args["from"]))


    data = []
    for x in mycursor.fetchall():
        ts = datetime.timestamp(x[0])
        data.append([ts,x[1],x[1]])
        

    if(args["from"] != "NaN"):
        print(data)

    # Create a PHP array and echo it as JSON

    # data = [time() * 1000, random() * 100,random() * 100]

    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response