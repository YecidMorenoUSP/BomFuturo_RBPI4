import bf_module.MySQL.config as CONFIG_MySQL


def connect():    
    import mysql.connector
    mydb = mysql.connector.connect(
        host=CONFIG_MySQL.host,
        user=CONFIG_MySQL.user,
        password=CONFIG_MySQL.password,
        database=CONFIG_MySQL.database
    )

    return mydb

def get_cursor():
    mydb = connect()
    cur = mydb.cursor()
    return cur