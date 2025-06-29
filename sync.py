import urequests
import ujson
from boot_config import API_URL, HEADERS
from storage import load_all, save, overwrite
from utils import debug

def try_post(reading):
    try:
        res = urequests.post(API_URL, headers=HEADERS, data=ujson.dumps(reading))
        debug(f"POST response: {res.status_code}")
        res.close()
        return res.status_code == 201
    except Exception as e:
        debug(f"Error posting data: {e}")
        return False

def resend_unsent():
    lines = load_all()
    remaining = []

    for line in lines:
        reading = ujson.loads(line)
        if not try_post(reading):
            remaining.append(line)

    overwrite(remaining)

def sync_reading(reading):
    debug(f"syncing reading: {reading}")
    resend_unsent()
    if not try_post(reading):
        save(reading)
