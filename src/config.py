import json
from pathlib import Path

def load_config(path):
    pth = Path(path)
    
    if pth.exists():
        with pth.open('r') as f:
            return json.load(f)
    else:
        raise FileNotFoundError(f'No config file found - {path}')