from flask import Flask, render_template_string
import json
import paho.mqtt.client as mqtt
from queue import Queue
from threading import Thread

TOPIC = "+/env"
QOS = 1

CONFIG_PATH = 'src/master_node/master.config.json'

event_queue = Queue()
room_status = {}

def load_config():
    with open(CONFIG_PATH, mode='r') as file:
        return json.load(file)

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
    event_queue.put(data_in)
    
def start_mqtt():
    config = load_config()

    client = mqtt.Client(protocol=mqtt.MQTTv5, client_id =config['id'])
    client.username_pw_set(username = config['mqtt']['username'], password=config['mqtt']['password'])
    
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    
    client.connect(config['mqtt']['ip'], config['mqtt']['port'], 60)
    client.loop_forever()
    
def update_room_status():
    while not event_queue.empty():
        evt = event_queue.get()
        room_status[evt['room']] = evt['status']
    
app = Flask(__name__)

HTML = """
<html>
<head>
    <title>Indoor Comfort Dashboard</title>
</head>

<body>
    <h1>Indoor Comfort Monitoring</h1>
    {% for room, status in data.items() %}
    <div>
        <strong>{{room}}</strong> : {{status}}
    </div>
    {% endfor %}
</body>
</html>
"""

@app.route("/")
def dashboard_ui():
    update_room_status()
    return render_template_string(HTML, data=room_status)

def main():
    Thread(target=start_mqtt, daemon=True).start()
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()