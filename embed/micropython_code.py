import network
import urequests
import time
from machine import Pin
from dht import DHT22



class Sensor:
    def __init__(self, pin):
        """Initialize the sensor with the given GPIO pin."""
        self.pin = Pin(pin, Pin.IN, Pin.PULL_UP)
        self.sensor = DHT22(self.pin)
        time.sleep(2)

    def read_data(self):
        """Read and return the temperature and humidity."""
        try:
            self.sensor.measure()
            temperature = self.sensor.temperature()#get temperature
            humidity = self.sensor.humidity()#get humidity
            return temperature, humidity
        except Exception as e:
            print(f"[Sensor] Error reading sensor data on pin {self.pin}: {e}")
            return None, None


class WiFi:
    def __init__(self, ssid, password):
        """Initialize the Wi-Fi connection with SSID and password."""
        self.ssid = ssid
        self.password = password

    def connect(self, timeout=30):
        """Connect to the Wi-Fi network with a timeout."""
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(self.ssid, self.password)
        print("[WiFi] Connecting to Wi-Fi...")
        start_time = time.time()

        while not wlan.isconnected():
            if time.time() - start_time > timeout:
                raise RuntimeError("[WiFi] Failed to connect to Wi-Fi within timeout period.")
            time.sleep(1)

        print("[WiFi] Connected to Wi-Fi!")
        print("[WiFi] IP address: 4.231.237.109")


class Backend:
    def __init__(self, server_url):
        """Initialize the backend with the server URL."""
        self.server_url = server_url

    def send_data(self, sensor_id, temperature, humidity):
        """Send the data to the backend using a POST request."""
        data = {
            "sensor_id": sensor_id,
            "temperature": temperature,
            "humidity": humidity,
            "timestamp": time.time()
        }
        try:
            response = urequests.post(self.server_url, json=data)
            if response.status_code == 200:
                print(f"[Backend] Data sent successfully")
            else:
                print(f"[Backend] Failed to send data. Status code: {response.status_code}, Response: {response.text}")
        except Exception as e:
            print(f"[Backend] Error sending data to server for Sensor {sensor_id}: {e}")


class SmartEnvMonitor:
    def __init__(self, ssid, password, sensor_pins, server_url):
        """Initialize the Smart Environmental Monitoring System."""
        self.wifi = WiFi(ssid, password)
        self.sensors = [Sensor(pin) for pin in sensor_pins]
        self.backend = Backend(server_url)

    def run(self):
        """Start the monitoring system."""
        #wifi connection
        self.wifi.connect()

        while True:
            for idx, sensor in enumerate(self.sensors):
                temperature, humidity = sensor.read_data()
                if temperature is not None and humidity is not None:
                    print(f"[Monitor] Sensor {idx + 1} - Temperature: {temperature}°C, Humidity: {humidity}%")
                    self.backend.send_data(idx + 1, temperature, humidity)
                else:
                    print(f"[Monitor] Sensor {idx + 1} failed to read data.")

            #10s for reading
            time.sleep(10)

ssid = "Wokwi-GUEST"
password = ""
server_url = "http://4.231.237.109/api/data"

#Pins for sensors
sensor_pins = [10, 15]

monitor = SmartEnvMonitor(ssid, password, sensor_pins, server_url)
monitor.run()
