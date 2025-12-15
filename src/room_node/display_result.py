import time
import pandas as pd
import numpy as np
from sense_hat import SenseHat

PATH = './src/room_node/logs/status.csv'
WINDOW = 1

sense = SenseHat()

def load_results():
    df = pd.read_csv(PATH, header=None, names=['status'])
    
    if len(df) < WINDOW:
        return None
        
    return df.tail(1)[["status"]].values.astype(str)[0][0]

while True:
    data = load_results()
    
    if data is None:
        time.sleep(5)
        continue
        
    print(data)
    sense.show_message(data)
    
    time.sleep(5)
    
    