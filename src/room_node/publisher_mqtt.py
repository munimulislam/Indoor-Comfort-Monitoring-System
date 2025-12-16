import json
import time
import pandas as pd
import paho.mqtt.client as mqtt

PUBLISH_INTERVAL = 5
QOS = 1
WINDOW = 1

STATUS_PATH = './src/room_node/logs/status.csv'
CONFIG_PATH = 'src/room_node/room.config.json'

def load_config():
    with open(CONFIG_PATH, mode='r') as file:
        return json.load(file) 

def load_results():
    df = pd.read_csv(STATUS_PATH, header=None, names=['status'])
    
    if len(df) < WINDOW:
        return None
        
    return df.tail(1)[["status"]].values.astype(str)[0][0]

def main():
    config = load_config()
    
    client = mqtt.Client(protocol=mqtt.MQTTv5, client_id =config['id'])
    client.username_pw_set(username = config['mqtt']['username'], password=config['mqtt']['password'])
    client.connect(config['mqtt']['ip'], config['mqtt']['port'], 60)
    client.reconnect_delay_set(min_delay = 1, max_delay=120)
    client.loop_start()
    
    try:
        while True:
            data = load_results()
    
            if data is None:
                continue
            
            payload = {
                'room': config['id'],
                'status': data
            }

            client.publish(f'{config['id']}/env', json.dumps(payload), qos=QOS)
            print(f"published: {payload}")
            
            time.sleep(PUBLISH_INTERVAL)
            
    except KeyboardInterrupt:
        print('Stopped data streaming')
            
    finally:
        client.loop_stop()
        client.disconnect()
            
if __name__ == '__main__':
    main()