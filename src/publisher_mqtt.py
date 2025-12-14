import json
import time
import paho.mqtt.client as mqtt

from sensor import sense_env_data

MASTER_IP = '192.168.0.17'
PORT = 1883
TOPIC = 'room_1/env'
PUBLISH_INTERVAL = 5
QOS = 1

def main():
    client = mqtt.Client(protocol=mqtt.MQTTv5, client_id ='room1')
    client.username_pw_set(username = 'room1', password='room1')
    client.connect(MASTER_IP, PORT, 60)
    client.loop_start()
    
    try:
        while True:
            data = sense_env_data()
            print(f"published: {data}")

            client.publish(TOPIC, json.dumps(data), qos=QOS)
            time.sleep(PUBLISH_INTERVAL)
            
    except KeyboardInterrupt:
        print('Stopped data streaming')
            
    finally:
        client.loop_stop()
        client.disconnect()
            
if __name__ == '__main__':
    main()