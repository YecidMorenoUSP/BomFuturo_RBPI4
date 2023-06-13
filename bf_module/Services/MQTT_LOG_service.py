
import json

from paho.mqtt import client as mqtt_client

import bf_module.MQTT.common  as MQTT
import bf_module.MQTT.config as CONFIG_MQTT


TAG = "[MQTT_DB_Service]"
client_id = "raspberry_bf"

def on_message(client, userdata, msg:mqtt_client.MQTTMessage):
    print(f"[{msg.topic}] : {msg.payload.decode()}")



def subscribe(client: mqtt_client.Client):
    client.subscribe(CONFIG_MQTT.topic_all)
    client.on_message = on_message

    

def run():
    client = MQTT.connect_mqtt(client_id)
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    print(f"{TAG}:init")
    run()
    print(f"{TAG}:end")