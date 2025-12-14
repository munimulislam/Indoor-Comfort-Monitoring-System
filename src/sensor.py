from sense_hat import SenseHat
import time
import os
import csv

sense = SenseHat()
FILE_PATH = '../data/env.csv'    

def log_data(interval=5):
    try:
        if not os.path.exists(FILE_PATH):
            write_csv_row(FILE_PATH, ["timestamp", "temparature", "humidity", "pressure"])
        
        while True:
            sensor_data = sense_data()
            write_csv_row(FILE_PATH, sensor_data) 
            time.sleep(interval)

    except KeyboardInterrupt:
        print('Data Logging Stopped')
        
def write_csv_row(path, data):
    try:
        with open(path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    except:
            print('Data coulod not be logged')

        
def sense_data():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    temparature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()

    return [timestamp, f"{temparature:.3f}", f"{humidity:.1f}", f"{pressure:.3f}"]
            
log_data()