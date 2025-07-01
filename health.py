import urequests
import time
import gc
import network_utils
from boot_config import DEVICE_ID, DEVICE_URL
from device import get_runtime_config

HEALTH_ENDPOINT = f"{DEVICE_URL}/{DEVICE_ID}/health"
config = get_runtime_config()
HEALTH_INTERVAL = config.get("reportIntervalSeconds", 300)

def get_firmware_version():
    # TODO: Return actual firmware version here (hardcode or from config)
    return "0.0.1"

def get_battery_level():
    # TODO: Implement actual measurement if we have battery monitoring hardware
    return None

# TODO: Implement actual measurement
def get_signal_strength():
    if network_utils and hasattr(network_utils, "get_signal_strength"):
        try:
            return network_utils.get_signal_strength()
        except Exception as e:
            print("Signal strength error:", e)
            return None
    return None

def send_health():
    payload = {
        "firmwareVersion": get_firmware_version(),
        "batteryLevel": get_battery_level(),
        "signalStrength": get_signal_strength(),
    }
    headers = {"Content-Type": "application/json"}
    try:
        resp = urequests.post(HEALTH_ENDPOINT, json=payload, headers=headers)
        resp.close()
        print("[health] Sent:", payload)
    except Exception as e:
        print("[health] Failed to send health data:", e)
    gc.collect()
