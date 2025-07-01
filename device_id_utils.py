import network
import os

BOOT_CONFIG_PATH = "boot_config.py"

def get_mac():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    mac = wlan.config('mac')
    return ''.join('{:02X}'.format(b) for b in mac)

def generate_device_id(mac):
    return f"pico-zone-sensor-{mac}"

def device_id_exists():
    try:
        with open(BOOT_CONFIG_PATH, "r") as f:
            return any("DEVICE_ID" in line for line in f)
    except OSError:
        return False

def write_device_id(device_id):
    lines = []
    try:
        with open(BOOT_CONFIG_PATH, "r") as f:
            lines = f.readlines()
    except OSError:
        pass

    with open(BOOT_CONFIG_PATH, "w") as f:
        # Rewrite each line in the config except old DEVICE_ID
        for line in lines:
            if not line.startswith("DEVICE_ID"):
                f.write(line)
        f.write(f"DEVICE_ID = '{device_id}'\n")

def init_device_id():
    if not device_id_exists():
        mac = get_mac()
        device_id = generate_device_id(mac)
        write_device_id(device_id)