try:
    import os
    from flask import Flask
    from flask import (Flask,
                       request,render_template,
                       redirect,
                       url_for,
                       session,
                       send_file)

    # from Website.Sensor.views import sensor_blueprint
    from www_bf.Humidity.views import humidity_blueprint
    from www_bf.Config.views import config_blueprint

    import bf_module.MySQL.config  as SQL_CONFIG

except Exception as e:
    print("Some Modules are Missing {}".format(e))

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
app.static_folder = 'static'

app.config['MYSQL_HOST'] = SQL_CONFIG.host
app.config['MYSQL_USER'] = SQL_CONFIG.user
app.config['MYSQL_PASSWORD'] = SQL_CONFIG.password
app.config['MYSQL_DB'] = SQL_CONFIG.database


app.register_blueprint(humidity_blueprint, url_prefix="/Humidity")
app.register_blueprint(config_blueprint, url_prefix="/Config")