import time
import signal
import sys
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

def on_shutdown(sig, frame):
    sense.clear()
    sys.exit(0)
    
signal.signal(signal.SIGINT, on_shutdown)
signal.signal(signal.SIGTERM, on_shutdown)

while True:
    data = load_results()
    
    if data is None:
        sense.clear(255, 255, 255)
        time.sleep(5)
        continue
            
    if data == 'GETTING UNCOMFORTABLE! TAKE ACTION':
        sense.clear(255, 0, 0)
    elif data == 'STARTING TO BE COMFORTABLE':
        sense.clear(0, 255, 0)
    else:
        sense.clear(255, 255, 255)
    
    time.sleep(5)
    
    