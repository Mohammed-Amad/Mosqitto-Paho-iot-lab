import paho.mqtt.client as mqtt
import time
import random

BROKER_ADDRESS = "localhost"
BROKER_PORT = 1883
TOPIC = "sensors/people"
STUDENT_ID = "12218857"

QOS_LEVEL = 1
RETAIN_FLAG = False

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected to MQTT Broker (PEOPLE publisher)")
    else:
        print(f"Failed to connect, return code {rc}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id="PeoplePublisher")
client.on_connect = on_connect

client.connect(BROKER_ADDRESS, BROKER_PORT)
client.loop_start()

try:
    while True:
        people_count = random.randint(0, 30)
        message = f"ID={STUDENT_ID}, PeopleCount={people_count}"

        result = client.publish(
            TOPIC,
            payload=message,
            qos=QOS_LEVEL,
            retain=RETAIN_FLAG
        )

        status = result.rc
        if status == 0:
            print(f"Sent `{message}` to `{TOPIC}` [qos={QOS_LEVEL}, retain={RETAIN_FLAG}]")
        else:
            print(f"Failed to send message to topic {TOPIC}")
        time.sleep(5)

except KeyboardInterrupt:
    print("PEOPLE publishing stopped.")
    client.loop_stop()
    client.disconnect()
