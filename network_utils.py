import network
import time
from config import SSID, PASSWORD

def connect_wifi(ssid=SSID, password=PASSWORD):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to wi-fi...")
        wlan.connect(ssid, password)
        timeout = 10
        while not wlan.isconnected() and timeout > 0:
            time.sleep(1)
            timeout -= 1
    print("Connected:", wlan.ifconfig())
