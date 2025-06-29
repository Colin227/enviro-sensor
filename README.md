# 🌱 Enviro-Sensor

A MicroPython-based environmental sensor system designed for Raspberry Pi Pico W. This project monitors **soil moisture**, **temperature**, and **humidity**, and sends the data to a backend API over Wi-Fi. It supports **offline caching**, **config sync from the backend**, and **dynamic updates** like report interval and debug mode.

---

## 📦 Features

- 🌡️ Reads temperature, humidity, and soil moisture
- 📡 Sends readings to a remote NestJS API
- ⚙️ Fetches and applies configuration updates (e.g., interval, debug mode)
- 📴 Caches failed readings and resends when back online
- 🔁 Hot-reloads config on-the-fly
- 🔌 Designed for use with solar or battery-powered setups

---

## 📁 File Structure
```
├── boot.py # Loads networking setup
├── device.py # Runtime config handling and hot reload
├── main.py # Main loop
├── network_utils.py # Connect to Wi-Fi
├── sensor.py # Reads sensor values
├── storage.py # Simple key-value and line storage for unsent data
├── sync.py # Syncs readings, handles caching
├── utils.py # Debug and helper functions
├── boot_config.py # Static boot config (Wi-Fi, API URLs, device ID)
├── runtime_config.json # Runtime config fetched from backend
```
---

## 🔧 Configuration

### `boot_config.py`

Set static values like:

```python
ZONE_ID = 0
SSID = "your-wifi"
PASSWORD = "your-password"
CONFIG_URL = "http://your.backend/config"
API_URL = "http://your.backend/api"
HEADERS = { "Content-Type": "application/json" }
DEVICE_ID = "your-device-id"
