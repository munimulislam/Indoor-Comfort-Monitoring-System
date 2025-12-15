DISPLAY_MODE_ADJUST = 'adjust'
DISPLAY_MODE_LOG = 'log'

FILE_PATH = "src/room_node/display_mode.txt"

def read_mode():
    with open(FILE_PATH, mode='r') as file:
        return file.read().strip()

def write_mode(mode):
    with open(FILE_PATH, mode='w') as file:
        file.write(mode)

def is_adjust_mode():
    return read_mode() == DISPLAY_MODE_ADJUST

def is_status_mode():
    return read_mode() == DISPLAY_MODE_LOG

def set_adjust_mode():
    write_mode(DISPLAY_MODE_ADJUST)
    
def set_status_mode():
    write_mode(DISPLAY_MODE_LOG)



