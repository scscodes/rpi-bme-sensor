# RPI Barometric Sensor Feed

[Original Reference & Inspiration](https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/2)

## Setup
- Create directory to store your file(s)
- Install required packages `bme280` `smbus2`
- Set `address` variable (try 0x76, 0x78)
  - If needed, run `sudo i2cdetect -y 1` to get it
- Set `refresh_interval` to delay updates, in seconds

## Start
- `python sensor.py` or your local equivalent

## Stop
- Keyboard interrupt `ctrl+C`, or
- Remove power cable from RPI

## Output
```json
{
  "Timestamp": "2024-08-05 21:28:51",
  "Humidity": "55.0%",
  "Pressure": "979.15 hPa (Low)",
  "Temperature": {
      "Celsius": "27.47",
      "Fahrenheit": "81.45"
  }
}
```