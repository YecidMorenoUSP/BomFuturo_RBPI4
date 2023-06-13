
import json

from paho.mqtt import client as mqtt_client

import bf_module.MQTT.common  as MQTT
import bf_module.MQTT.config as CONFIG_MQTT

import bf_module.MySQL.common as MySQL

TAG = "[MQTT_Service]"

client_id = "raspberry_bf"

def on_humidity(client, userdata, msg):
    
    
    data = json.loads(msg.payload.decode())

    if "humidity" in data and "sensor_id" in data:
        
        print(f"[{msg.topic}] : {msg.payload.decode()}")

        H = data.get("humidity")
        id = data.get("sensor_id")
        
        mycursor = mydb.cursor()
        sql = "INSERT INTO humidity_reads (sensor_id, value) VALUES (%s,%s)"
        val = (id, H)
        mycursor.execute(sql, val)
        mydb.commit()



def subscribe(client: mqtt_client):
    client.subscribe(CONFIG_MQTT.topic_humidity)
    client.on_message = on_humidity

def run():
    client = MQTT.connect_mqtt(client_id)
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    print(f"{TAG}:init")
    mydb = MySQL.connect()
    run()
    print(f"{TAG}:end")