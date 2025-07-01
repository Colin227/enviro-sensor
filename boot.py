from device_id_utils import init_device_id
from network_utils import connect_wifi
from utils import debug

init_device_id()
connect_wifi()
debug("Boot complete.")