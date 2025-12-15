import time
import pandas as pd
import numpy as np
from sense_hat import SenseHat

PATH = './src/room_node/logs/status.csv'
WINDOW = 1

sense = SenseHat()

def load_data():
    df = pd.read_csv(PATH, header=None, names=['status'])
    
    if len(df) < WINDOW:
        return None
        
    return df.tail(1)[["status"]].values.astype(str)[0][0]

def display_status(data):
    sense.show_message(data)

while True:
    data = load_data()
    
    if data is None:
        time.sleep(5)
        continue
        
    print(data)
    display_status(data)
    time.sleep(5)