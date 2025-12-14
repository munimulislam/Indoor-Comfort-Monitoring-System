import json
import paho.mqtt.client as mqtt
from config import load_config

TOPIC = "+/env"
QOS = 1

def on_connect(client, data, flags, reason_code, props):
    if reason_code == 0:
        print("connected to broker")
        client.subscribe(TOPIC)
    else:
        print(f'Connection Failed! {reason_code}')

def on_disconnect(client, data, reason_code):
    if reason_code != 0:
        print('Retrying connection...')
    else:
        print('disconbnected from broker!')

def on_message(client, data, msg):
    data_in = json.loads(msg.payload.decode())
    print(data_in)
    
def main():
    config = load_config('./config/master.config.json')
    print(config)

    client = mqtt.Client(protocol=mqtt.MQTTv5, client_id =config['id'])
    client.username_pw_set(username = config['mqtt']['username'], password=config['mqtt']['password'])
    
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    
    client.connect(config['mqtt']['ip'], config['mqtt']['port'], 60)
    client.loop_forever()
    
if __name__ == '__main__':
    main()