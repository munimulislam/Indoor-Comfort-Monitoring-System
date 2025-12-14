import json
import time
import paho.mqtt.client as mqtt

from sensor import sense_data

MASTER_IP = '192.168.0.17'
PORT = 1883
TOPIC = 'room_1/env'
PUBLISH_INTERVAL = 5
QOS = 1

def main():
    print('qsqsqs')
    client = mqtt.Client(protocol=mqtt.MQTTv5, client_id ='room1')
    client.connect(MASTER_IP, PORT, 60)
    client.loop_start()
    
    try:
        while True:
            data = sense_data()
            client.publish(TOPIC, json.dumps(data), qos=QOS)
            print(f"published: {data}")
            time.sleep(PUBLISH_INTERVAL)
            
    except KeyboardInterrupt:
        print('Stopped data streaming')
            
    finally:
        print('final')
        client.loop_stop()
        client.disconnect()
            
if __name__ == '__main__':
    print('sdd')
    main()