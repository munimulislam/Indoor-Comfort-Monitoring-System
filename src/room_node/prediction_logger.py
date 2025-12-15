import time
import csv
import pandas as pd
import numpy as np
from forecast import get_prediction
from context import get_context

LOG_IN_PATH = './src/room_node/logs/env.csv'
LOG_OUT_PATH = './src/room_node/logs/status.csv'
WINDOW = 10

def load_data():
    df = pd.read_csv(LOG_IN_PATH)
    
    if len(df) < WINDOW:
        return None
    
    data = df.tail(WINDOW)[["temparature", "humidity"]].values.astype(np.float32)
    
    return data

def write_prediction(data):
    with open(LOG_OUT_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
        
open(LOG_OUT_PATH, "w").close()

while True:
    data = load_data()
    
    if data is None:
        time.sleep(5)
        continue
    
    x = np.expand_dims(data, axis=0)
    prediction = get_prediction(x)
    context = get_context(prediction)
    
    print(f'[LOG::PREDICTION LOGGER] {context}')
    write_prediction([context])
    time.sleep(5)
    