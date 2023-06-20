
import json

from paho.mqtt import client as mqtt_client

import bf_module.MQTT.common  as MQTT
import bf_module.MQTT.config as CONFIG_MQTT

import bf_module.MySQL.common as MySQL

TAG = "[MQTT_Service]"

client_id = "raspberry_bf"

def on_humidity(client, userdata, msg):
    
    print(f"[{msg.topic}] : {msg.payload.decode()}")

    required_keys = {"value","payload"}
    
    msg_topic = msg.topic.split("/");
    topic_id =  msg_topic[0]

    data = json.loads(msg.payload.decode())
    

    if(msg_topic[1] == "humidity"):    
        if required_keys.issubset(data.keys()):
            cur = mydb.cursor()
            cur.callproc("InsertSensorReading",(topic_id,data["value"],"{}"))
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