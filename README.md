
# Edge AI Indoor Comfort Monitoring System

This project implements an edge‑based indoor comfort monitoring system using Raspberry Pi and Sense HAT.
Each room runs local AI inference to analyse temperature, humidity, pressure, and motion data.
The system is context‑aware, supports user‑adjustable comfort thresholds, and uses MQTT middleware to share data securely with a master node.
The key idea is that each room works independently, even if the network or MQTT broker goes offline.

Key Features
 - Reads sensor data from the Sense HAT (temperature, humidity)
 - Runs an AI model locally to predict comfort/discomfort behaviour
 - Applies context awareness based on user‑defined comfort thresholds
 - Allows users to adjust comfort thresholds using the Sense HAT joystick
 - Publishes room data to a master node using MQTT with password        authentication
 - Continues working locally if MQTT connection fails


## Deployment

To deploy this project run

In All Nodes:
```bash
  sudo apt update
  sudo apt install -y python3-pip
  sudo apt-get install mosquitto mosquitto-clients paho-mqtt numpy pandas sense-hat
```

In Room Nodes:
```bash
  ./run_room.sh
```

In Master Node:
```bash
  sudo systemctl start mosquitto
  sudo systemctl enable mosquitto

  sudo mkdir -p /etc/mosquitto  
  sudo mosquitto_passwd /etc/mosquitto/passwd room1 #insert password
  sudo mosquitto_passwd /etc/mosquitto/passwd master #insert password
  sudo nano /etc/mosquitto/mosquitto.conf

  #Add these in configurationm file:
  listener 1883
  allow_anonymous false
  password_file /etc/mosquitto/passwd

  sudo systemctl restart mosquitto

  python3 main.py
```

## Joystick Control

 - Middle button Press: Enters Adjust Mode
 - Left/Right Button Press: Switches between Options (min_temparature, max_temparature, min_humidity, max_humidity)
 - Up Button Press: Increases temparature options by 0.5 and humidity options by 1
 - Down Button Press: Decreases temparature options by 0.5 and humidity options by 1
