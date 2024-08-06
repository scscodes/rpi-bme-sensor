import bme280
import smbus2
from time import sleep, strftime, localtime
import json
import os


def classify_pressure(pressure):
    if pressure > 1020:
        return "High"
    elif pressure < 1000:
        return "Low"
    else:
        return "Medium"


def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')


def read_sensor_data(bus, address):
    bme280_data = bme280.sample(bus, address)

    humidity = round(bme280_data.humidity, 2)
    pressure = round(bme280_data.pressure, 2)
    ambient_temperature_c = round(bme280_data.temperature, 2)
    ambient_temperature_f = round((ambient_temperature_c * 9 / 5) + 32, 2)

    data = {
        "Timestamp": strftime("%Y-%m-%d %H:%M:%S", localtime()),
        "Humidity": f"{humidity}%",
        "Pressure": f"{pressure} hPa ({classify_pressure(pressure)})",
        "Temperature": {
            "Celsius": f"{ambient_temperature_c}",
            "Fahrenheit": f"{ambient_temperature_f}"
        }
    }

    return data


port = 1
address = 0x76
bus = smbus2.SMBus(port)
refresh_interval = 5

bme280.load_calibration_params(bus, address)

while True:
    sensor_data = read_sensor_data(bus, address)
    json_data = json.dumps(sensor_data, indent=4)
    clear_screen()
    print(json_data)
    sleep(refresh_interval)
