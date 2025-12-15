import json
import os
import time
from sense_hat import SenseHat
from display_mode import set_adjust_mode, set_status_mode

sense = SenseHat()

DIRECTION_MIDDLE = 'middle'
DIRECTION_UP = 'up'
DIRECTION_DOWN = 'down'
DIRECTION_LEFT = 'left'
DIRECTION_RIGHT = 'right'
ACTION_PRESSED = 'pressed'

ADJUST_OPTIONS = [('temp_max',0.5), ('temp_min',0.5), ('humidity_min',1), ('humidity_max',1)]

CONFIG_PATH = 'src/room_node/room.config.json'
adjusting = False

config = None
option_pos = 0

def load_config():
    with open(CONFIG_PATH, mode='r') as file:
        return json.load(file)
    
def save_config(config):
    with open(CONFIG_PATH, mode='w') as file:
        json.dump(config, file)

while True:
    for e in sense.stick.get_events():
        if e.action != ACTION_PRESSED:
            continue
            
        if not adjusting and e.direction == DIRECTION_MIDDLE:
            adjusting = True
            set_adjust_mode()
            sense.show_message('ADJUST')
            config = load_config()
            option_pos = 0
            continue
        
        if adjusting:
            if e.direction == DIRECTION_UP:
                option, step = ADJUST_OPTIONS[option_pos]
                config['comfort'][option] += step
                
            elif e.direction == DIRECTION_DOWN:
                option, step = ADJUST_OPTIONS[option_pos]
                config['comfort'][option] -= step
                
            elif e.direction == DIRECTION_LEFT:
                option_pos = len(ADJUST_OPTIONS) - 1 if option_pos == 0 else option_pos - 1
                
            elif e.direction == DIRECTION_RIGHT:
                option_pos = 0 if option_pos == len(ADJUST_OPTIONS) - 1 else option_pos + 1
                
            elif e.direction == DIRECTION_MIDDLE:
                save_config(config)
                sense.show_message('SAVED')
                sense.clear()
                set_status_mode()
                adjusting = False
                
                continue
            
            option, step = ADJUST_OPTIONS[option_pos]
            sense.show_message(f'{option}: {config['comfort'][option]}')
            