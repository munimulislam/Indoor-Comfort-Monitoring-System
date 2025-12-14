from sense_hat import SenseHat
import time
import os
import csv

sense = SenseHat()
        
def sense_env_data():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    temparature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()

    return [timestamp, f"{temparature:.3f}", f"{humidity:.1f}", f"{pressure:.3f}"]