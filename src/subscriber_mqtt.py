import json
import paho.mqtt.client as mqtt

HOST = 'localhost'
PORT = 1883
TOPIC = "+/env"
QOS = 1

def on_connect(client, data, flags, reason_code, props):
    if reason_code == 0:
        print("connected to broker")
        client.subscribe(TOPIC,QOS)

def on_message(client, data, msg):
    data_in = json.loads(msg.payload.decode())
    print(data_in)
    
def main():
    client = mqtt.Client(protocol=mqtt.MQTTv5)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, 60)
    client.loop_forever()
    
if __name__ == '__main__':
    main()