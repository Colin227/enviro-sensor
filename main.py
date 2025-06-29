from sensor import read_environment
from sync import sync_reading
from time import sleep

while True:
    reading = read_environment()
    sync_reading(reading)
    sleep(60)
