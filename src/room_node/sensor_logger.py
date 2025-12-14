import os
import csv
import time
from sensor import sense_env_data

FILE_PATH = './src/room_node/logs/env.csv'    

def log_data(interval=5):
    try:
        os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
        
        if not os.path.exists(FILE_PATH):
            write_csv_row(FILE_PATH, ["timestamp", "temparature", "humidity", "pressure"])
        
        while True:
            sensor_data = sense_env_data()
            write_csv_row(FILE_PATH, sensor_data) 
            time.sleep(interval)

    except KeyboardInterrupt:
        print('Data Logging Stopped')
    except FileNotFoundError:
        print('File Not Found')
        
def write_csv_row(path, data):
    try:
        with open(path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    except:
            print('Data coulod not be logged')
            
if __name__ == '__main__':
    log_data()