from boot_config import DEVICE_ID
from pmon import PlantMonitor
from utils import debug
import gc

pm = PlantMonitor()

def read_environment():
    reading = {
        "deviceId": DEVICE_ID,
        "moisture": pm.get_wetness(),
        "temperature": pm.get_temp(),
        "humidity": pm.get_humidity()
    }
    debug(f"Sensor reading: {reading}")
    gc.collect()
    return reading