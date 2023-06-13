import random
import time
import json

from paho.mqtt import client as mqtt_client

import bf_module.MQTT.config  as CONFIG

TAG = "[MQTT_RandomHumidity]: "
client_id = "esp32_random_humidity"

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client()
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(CONFIG.broker, CONFIG.port)
    return client

def publish_loop(client):
    msg_count = 0
    topic = CONFIG.topic_humidity
    
    

    while True:
        time.sleep(2)

        H = random.random()*20+40
        H = round(H,2)

        msg = {"sensor_id":100,
               "humidity":H}

        result = client.publish(topic, json.dumps(msg))
        status = result[0]
        if status == 0:
            print(f"{TAG} {json.dumps(msg)}")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
    None

if __name__ == '__main__':
    print(TAG+"init")
    
    client = connect_mqtt()
    client.loop_start()

    publish_loop(client)

    print(TAG+"end")