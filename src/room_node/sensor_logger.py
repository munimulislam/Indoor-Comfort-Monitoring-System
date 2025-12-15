import os
import csv
import time
from sensor import sense_env_data

FILE_PATH = './src/room_node/logs/env.csv'
MAX_ROWS = 1000

def log_data(interval=5):
    try:
        open(FILE_PATH, "w").close()
        write_csv_row(["timestamp", "temparature", "humidity"])
            
        while True:
            trim_log()
            sensor_data = sense_env_data()
            write_csv_row(sensor_data) 
            time.sleep(interval)

    except KeyboardInterrupt:
        print('Data Logging Stopped')
    except FileNotFoundError:
        print('File Not Found')
        
def trim_log():
    with open(FILE_PATH, mode='r') as file:
        rows = file.readlines()
    
    header = rows[0]
    data = rows[1:]
    
    if len(data) > MAX_ROWS:
        data = data[-MAX_ROWS:]
        
    with open(FILE_PATH, mode='w') as file:
        file.write(header)
        file.writelines(data)
        
def write_csv_row(data):
    try:
        with open(FILE_PATH, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    except:
            print('Data coulod not be logged')
            
if __name__ == '__main__':
    log_data()