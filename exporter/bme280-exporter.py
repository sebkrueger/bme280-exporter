#!/usr/bin/python3
from prometheus_client import start_http_server, Gauge
from adafruit_bme280 import basic as adafruit_bme280

import time
import board
import busio
import random

i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x77)

# Erstellen eines Metrics-Objekts
temperature = Gauge('temperature', 'Temperature in degree C')
humidity = Gauge('humidity', 'absolut humidity in %')
relative_humidity = Gauge('relative_humidity', 'absolut humidity in %')
pressure = Gauge('pressure', 'absolut pressure in hPa')

def process_request():
    bme280.mode = adafruit_bme280.MODE_NORMAL
    """BME 280 Sensordata"""

    temperature.set(bme280.temperature)  
    humidity.set(bme280.humidity) 
    relative_humidity.set(bme280.relative_humidity)
    pressure.set(bme280.pressure)
    
if __name__ == '__main__':
    # start server on port 8000
    start_http_server(8000)
    while True:
        process_request()
        # wait between updates
        time.sleep(10)
