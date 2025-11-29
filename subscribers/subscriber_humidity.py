import paho.mqtt.client as mqtt
from datetime import datetime

BROKER_ADDRESS = "localhost"
BROKER_PORT = 1883
TOPIC = "sensors/humidity"

def on_connect(client, userdata, flags, rc, properties=None):
    print("HUMIDITY subscriber connected, rc =", rc)
    client.subscribe(TOPIC, qos=1)

def on_message(client, userdata, msg):
    now = datetime.now().strftime("%H:%M:%S")
    payload = msg.payload.decode()
    print(
        f"[{now}] HUMIDITY -> Message={payload}, "
        f"QoS={msg.qos}, Retain={msg.retain}"
    )

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id="HumiditySubscriber")
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_ADDRESS, BROKER_PORT, 60)
print("HUMIDITY subscriber started ...")
client.loop_forever()
