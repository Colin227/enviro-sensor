from config import DEVICE_ID
from pmon import PlantMonitor

pm = PlantMonitor()

def read_environment():
    return {
        "deviceId": DEVICE_ID,
        "moisture": pm.get_wetness(),
        "temperature": pm.get_temp(),
        "humidity": pm.get_humidity()
    }