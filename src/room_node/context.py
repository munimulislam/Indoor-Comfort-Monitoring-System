import json
import os

ROOM_CONFIG_PATH = './src/room_node/room.config.json'

def load_config():
    with open(ROOM_CONFIG_PATH, mode='r') as file:
        return json.load(file)

def get_context(pred):
    """
        convert numeric prediction into displayable string by comparing with user context
    """
    if pred is None:
        return "CALCULATING. PLEASE WAIT!"

    config = load_config()
    comfort_data = config['comfort']
    
    pred_t, pred_h = pred

    risk = pred_t < comfort_data["temp_min"] or pred_t > comfort_data["temp_max"] or pred_h < comfort_data["humidity_min"] or pred_h > comfort_data["humidity_max"]

    return "GETTING UNCOMFORTABLE! TAKE ACTION" if risk else "STARTING TO BE COMFORTABLE"