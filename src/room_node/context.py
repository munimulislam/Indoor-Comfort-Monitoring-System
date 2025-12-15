import json
from pathlib import Path

def load_config(path):
    pth = Path(path)
    
    if pth.exists():
        with pth.open('r') as f:
            return json.load(f)
    else:
        raise FileNotFoundError(f'No config file found - {path}')
    
def get_context(pred):
    if pred is None:
        return "CALCULATING. PLEASE WAIT!", None

    config = load_config('./src/room_node/room.config.json')
    comfort_data = config['comfort']
    pred_t, pred_h = pred

    risk = pred_t < comfort_data["temp_min"] or pred_t > comfort_data["temp_max"] or pred_h < comfort_data["humidity_min"] or pred_h > comfort_data["humidity_max"]

    return "Getting Uncomfortable" if risk else "COMFORTABLE"