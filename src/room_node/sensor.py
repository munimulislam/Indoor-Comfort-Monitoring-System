from sense_hat import SenseHat
import time

sense = SenseHat()
        
def sense_env_data():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    temparature = sense.get_temperature()
    humidity = sense.get_humidity()

    return [timestamp, f"{temparature:.3f}", f"{humidity:.1f}"]