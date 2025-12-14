import json
import time
import paho.mqtt.client as mqtt

from sensor import sense_env_data
from config import load_config

PUBLISH_INTERVAL = 5
QOS = 1

def main():
    config = load_config('../config/room1.config.json')
    
    client = mqtt.Client(protocol=mqtt.MQTTv5, client_id =config.id)
    client.username_pw_set(username = config.mqtt.username, password=config.mqtt.password)
    client.connect(config.mqtt.ip, config.mqtt.port, 60)
    client.loop_start()
    
    try:
        while True:
            time, temp, hum, press = sense_env_data()
            payload = {
                'timestamp': time,
                'room': ROOM,
                'temparature': temp,
                'himidity': hum,
                'pressure': press
            }

            client.publish(f'{config.id}/env', json.dumps(payload), qos=QOS)
            print(f"published: {payload}")
            
            time.sleep(PUBLISH_INTERVAL)
            
    except KeyboardInterrupt:
        print('Stopped data streaming')
            
    finally:
        client.loop_stop()
        client.disconnect()
            
if __name__ == '__main__':
    main()