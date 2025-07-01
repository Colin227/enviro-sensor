import urequests
import ujson
from boot_config import CONFIG_URL
from utils import debug, set_debug

RUNTIME_CONFIG_PATH = "runtime_config.json"
_config_cache = {}

def get_remote_config(device_id):
    try:
        url = f"{CONFIG_URL}/devices/{device_id}/config"
        response = urequests.get(url)
        if response.status_code == 200:
            config = response.json()
            print("Fetched config:", config)
            return config
        else:
            print("Failed to fetch config:", response.status_code)
    except Exception as e:
        print("Config fetch error:", e)
    return {}

def apply_new_config(config):
    global _config_cache
    try:
        with open(RUNTIME_CONFIG_PATH, "w") as f:
            f.write(ujson.dumps(config))
        _config_cache = config
        set_debug(config.get("debugMode", False))
        debug("Applied new config and updated config debug mode.")
    except Exception as e:
        debug(f"Failed to apply config: {e}")

def load_runtime_config(device_id):
    global _config_cache
    config = get_remote_config(device_id)
    if config:
        apply_new_config(config)
        return config
    
    # Fallback handling uses local file
    try:
        with open(RUNTIME_CONFIG_PATH, "r") as f:
            _config_cache = ujson.loads(f.read())
            debug(f"Loaded local config: {_config_cache}")
            return _config_cache
    except:
        print("No valid config found")
        return {}

def get_runtime_config():
    global _config_cache
    return _config_cache or {}