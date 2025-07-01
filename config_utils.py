from time import time, sleep
from device import apply_new_config, get_remote_config
from health import send_health
import _thread

_config_cache = {}

def start_config_and_health_watcher(device_id, config_interval=300, health_interval=300):
    def watcher():
        global _config_cache
        last_config_time = 0
        last_health_time = 0

        while True:
            now = time()

            if now - last_config_time >= config_interval:
                remote_config = get_remote_config(device_id)
                if remote_config and remote_config != _config_cache:
                    apply_new_config(remote_config)
                last_config_time = now

            if now - last_health_time >= health_interval:
                send_health()
                last_health_time = now
            
            sleep(1)
    _thread.start_new_thread(watcher, ())   