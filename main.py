from sensor import read_environment
from sync import sync_reading
from time import sleep
from device import load_runtime_config, start_config_watcher, get_runtime_config
from boot_config import DEVICE_ID
from utils import debug, set_debug

config = load_runtime_config(DEVICE_ID)
current_debug = config.get("debugMode", False)
set_debug(current_debug)



start_config_watcher(DEVICE_ID, interval_sec=300) # Sync config with remote every 5 mins

while True:
    reading = read_environment()
    sync_reading(reading)
    config = get_runtime_config()
    interval = config.get("reportIntervalSeconds", 60) # Fallback to 60 second intervals

    new_debug = config.get("debugMode", False)
    if new_debug != current_debug:
        set_debug(new_debug)
        current_debug = new_debug
        debug(f"Debug mode updated to: {new_debug}")

    debug(f"Sleeping for {interval} seconds...")
    sleep(interval)
