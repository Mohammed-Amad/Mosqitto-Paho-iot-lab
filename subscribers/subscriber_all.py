import paho.mqtt.client as mqtt
from datetime import datetime

BROKER_ADDRESS = "localhost"
BROKER_PORT = 1883
TOPIC_FILTER = "sensors/#"   
def on_connect(client, userdata, flags, rc, properties=None):
    print("ALL subscriber connected, rc =", rc)
    client.subscribe(TOPIC_FILTER, qos=1)

def on_message(client, userdata, msg):
    now = datetime.now().strftime("%H:%M:%S")
    payload = msg.payload.decode()
    print(
        f"[{now}] Topic={msg.topic}, "
        f"Message={payload}, "
        f"QoS={msg.qos}, Retain={msg.retain}"
    )

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id="AllSubscriber")
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_ADDRESS, BROKER_PORT, 60)
print("ALL subscriber started ...")
client.loop_forever()
