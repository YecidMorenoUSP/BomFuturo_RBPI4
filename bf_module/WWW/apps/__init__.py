try:
    import os
    from flask import Flask
    from flask import (Flask,
                       request,render_template,
                       redirect,
                       url_for,
                       session,
                       send_file)

    # from apps.Config.views import sensor_blueprint
    # from apps.Humidity.views import humidity_blueprint
    # from apps.Config.views import config_blueprint

    import bf_module.MySQL.config  as SQL_CONFIG
    from importlib import import_module

except Exception as e:
    print("Some Modules are Missing {}".format(e))

# app = Flask(__name__)
# app.config["SECRET_KEY"] = "mysecretkey"

# app.config['MYSQL_HOST'] = SQL_CONFIG.host
# app.config['MYSQL_USER'] = SQL_CONFIG.user
# app.config['MYSQL_PASSWORD'] = SQL_CONFIG.password
# app.config['MYSQL_DB'] = SQL_CONFIG.database
# app.config['ASSETS_ROOT'] = '/static/assets'
# app.static_folder = 'static'


def register_blueprints(app):
    None
    # app.register_blueprint(humidity_blueprint, url_prefix="/Humidity")
    # app.register_blueprint(config_blueprint, url_prefix="/Config")

    for module_name in ["home"]:
        module = import_module(f'apps.{module_name}.routes')
        app.register_blueprint(module.blueprint)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_blueprints(app)
    return app