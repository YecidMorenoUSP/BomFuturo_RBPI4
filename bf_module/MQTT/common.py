
from paho.mqtt import client as mqtt_client
import bf_module.MQTT.config as CONFIG_MQTT

def connect_mqtt(client_id):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(CONFIG_MQTT.broker, CONFIG_MQTT.port)
    return client