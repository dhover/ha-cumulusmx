"""Constants for the CumulusMX integration."""

from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from homeassistant.const import (
    UnitOfTemperature,
    UnitOfPressure,
    UnitOfLength,
    UnitOfSpeed,
    UnitOfVolumetricFlux,
    CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    PERCENTAGE,
    DEGREE,
)

# Constants for CumulusMX integration

DOMAIN = "cumulusmx"

CONF_UPDATE_INTERVAL = "update_interval"
CONF_HOST = "host"
CONF_PORT = "port"
CONF_WEBTAGS = "webtags"

DEFAULT_HOST = "192.168.x.x"
DEFAULT_PORT = 8998
DEFAULT_WEBTAGS = "temp,hum,dew,heatindex,press,rfall,rrate,wgust," \
                    "wspeed,wlatest,wdir,currentwdir,bearing," \
                    "avgbearing,LastRainTipISO,AirLinkPm1Out," \
                    "AirLinkPm2p5Out,AirLinkPm2p5_1hrOut," \
                    "AirLinkPm2p5_3hrOut,AirLinkPm2p5_24hrOut," \
                    "AirLinkPm2p5_NowcastOut,AirLinkPm10Out," \
                    "AirLinkPm10_1hrOut,AirLinkPm10_3hrOut," \
                    "AirLinkPm10_24hrOut,AirLinkPm10_NowcastOut," \
                    "AirLinkAqiPm2p5Out,AirLinkAqiPm2p5_1hrOut," \
                    "AirLinkAqiPm2p5_3hrOut,AirLinkAqiPm2p5_24hrOut," \
                    "AirLinkAqiPm2p5_NowcastOut,AirLinkAqiPm10Out," \
                    "AirLinkAqiPm10_1hrOut,AirLinkAqiPm10_3hrOut," \
                    "AirLinkAqiPm10_24hrOut,AirLinkAqiPm10_NowcastOut," \
                    "AirLinkTempOut,AirLinkHumOut,MulticastGoodCnt," \
                    "MulticastBadCnt,MulticastGoodPct,ProgramUpTime," \
                    "SystemUpTime,version,build,timehhmmss,txbattery tx=1,txbattery tx=2"
DEFAULT_UPDATE_INTERVAL = 60

# Endpoint for reading sensors
SENSOR_API_URL = "http://{host}:{port}/api/tags/process.txt"
GITHUB_API_URL = "https://api.github.com/repos/cumulusmx/cumulusmx/releases/latest"

SENSOR_TYPES = {
    # Sensors for Airlink device
    "airlinkpm1out": {
        "device": "airlink", "name": "PM 1.0",
        "device_class": SensorDeviceClass.PM1,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
    },
    "airlinkpm2p5out": {
        "device": "airlink", "name": "PM 2.5",
        "device_class": SensorDeviceClass.PM25,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
    },
    "airlinkpm2p5_1hrout": {
        "device": "airlink", "name": "PM 2.5 1h",
        "device_class": SensorDeviceClass.PM25,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
    },
    "airlinkpm2p5_3hrout": {
        "device": "airlink", "name": "PM 2.5 3h",
        "device_class": SensorDeviceClass.PM25,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
    },
    "airlinkpm2p5_24hrout": {
        "device": "airlink", "name": "PM 2.5 24h",
        "device_class": SensorDeviceClass.PM25,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
    },
    "airlinkpm2p5_nowcastout": {
        "device": "airlink", "name": "Pm 2.5 Nowcast",
        "device_class": SensorDeviceClass.PM25,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
    },
    "airlinkpm10out": {
        "device": "airlink", "name": "PM 10",
        "device_class": SensorDeviceClass.PM10,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
    },
    "airlinkpm10_1hrout": {
        "device": "airlink", "name": "PM 10 1h",
        "device_class": SensorDeviceClass.PM10,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
    },
    "airlinkpm10_3hrout": {
        "device": "airlink", "name": "PM 10 3h",
        "device_class": SensorDeviceClass.PM10,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
    },
    "airlinkpm10_24hrout": {
        "device": "airlink", "name": "PM 10 24h",
        "device_class": SensorDeviceClass.PM10,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
    },
    "airlinkpm10_nowcastout": {
        "device": "airlink", "name": "PM 10 Nowcast",
        "device_class": SensorDeviceClass.PM10,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
    },
    "airlinkaqipm2p5out": {
        "device": "airlink", "name": "PM 2.5 AQI",
        "device_class": SensorDeviceClass.AQI,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": None
    },
    "airlinkaqipm2p5_1hrout": {
        "device": "airlink", "name": "PM 2.5 AQI 1h",
        "device_class": SensorDeviceClass.AQI,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": None
    },
    "airlinkaqipm2p5_3hrout": {
        "device": "airlink", "name": "PM 2.5 AQI 3h",
        "device_class": SensorDeviceClass.AQI,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": None
    },
    "airlinkaqipm2p5_24hrout": {
        "device": "airlink", "name": "PM 2.5 AQI 24h",
        "device_class": SensorDeviceClass.AQI,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": None
    },
    "airlinkaqipm2p5_nowcastout": {
        "device": "airlink", "name": "PM 2.5 AQI Nowcast",
        "device_class": SensorDeviceClass.AQI,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": None
    },
    "airlinkaqipm10out": {
        "device": "airlink", "name": "PM 10 AQI",
        "device_class": SensorDeviceClass.AQI,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": None
    },
    "airlinkaqipm10_1hrout": {
        "device": "airlink", "name": "PM 10 AQI 1h",
        "device_class": SensorDeviceClass.AQI,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": None
    },
    "airlinkaqipm10_3hrout": {
        "device": "airlink", "name": "PM 10 AQI 3h",
        "device_class": SensorDeviceClass.AQI,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": None
    },
    "airlinkaqipm10_24hrout": {
        "device": "airlink", "name": "PM 10 AQI 24h",
        "device_class": SensorDeviceClass.AQI,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": None
    },
    "airlinkaqipm10_nowcastout": {
        "device": "airlink", "name": "PM 10 AQI Nowcast",
        "device_class": SensorDeviceClass.AQI,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": None
    },
    "airlinkhumout": {
        "device": "airlink", "name": "Humidity",
        "device_class": SensorDeviceClass.HUMIDITY,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": PERCENTAGE
    },
    "airlinktempout": {
        "device": "airlink", "name": "Temperature",
        "device_class": SensorDeviceClass.TEMPERATURE,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfTemperature.CELSIUS
    },
    # Sensors for System Info device
    "build": {
        "device": "system", "name": "Build",
        "device_class": None,
        "state_class": None,
        "unit": None,
        "icon": "mdi:tools"
    },
    "multicastbadcnt": {
        "device": "system", "name": "Bad packets",
        "device_class": None,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "unit": None,
        "icon": "mdi:alert"
    },
    "multicastgoodcnt": {
        "device": "system", "name": "Good packets",
        "device_class": None,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "unit": None,
        "icon": "mdi:check-circle"
    },
    "multicastgoodpct": {
        "device": "system", "name": "Good packets percent",
        "device_class": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": PERCENTAGE,
        "icon": "mdi:percent"
    },
    "programuptime": {
        "device": "system", "name": "Uptime",
        "device_class": None,
        "state_class": None,
        "unit": None,
        "icon": "mdi:clock-outline"
    },
    "systemuptime": {
        "device": "system", "name": "System Uptime",
        "device_class": None,
        "state_class": None,
        "unit": None,
        "icon": "mdi:clock-outline"
    },
    "timehhmmss": {
        "device": "system", "name": "Time",
        "device_class": None,
        "state_class": None,
        "unit": None,
        "icon": "mdi:clock-time-four-outline"
    },
    "txbattery tx=1": {
        "device": "system", "name": "Battery ISS 1",
        "device_class": None,
        "state_class": None,
        "unit": None,
        "icon": "mdi:battery-outline"
    },
    "txbattery tx=2": {
        "device": "system", "name": "Battery ISS 2",
        "device_class": None,
        "state_class": None,
        "unit": None,
        "icon": "mdi:battery-outline"
    },
    "version": {
        "device": "system", "name": "Version",
        "device_class": None,
        "state_class": None,
        "unit": None,
        "icon": "mdi:information-outline"
    },
    # Sensors for Weather device (the rest)
    "avgbearing": {
        "device": "weather", "name": "Average Bearing",
        "device_class": SensorDeviceClass.WIND_DIRECTION,
        "state_class": SensorStateClass.MEASUREMENT_ANGLE,
        "unit": DEGREE
    },
    "bearing": {
        "device": "weather", "name": "Bearing",
        "device_class": SensorDeviceClass.WIND_DIRECTION,
        "state_class": SensorStateClass.MEASUREMENT_ANGLE,
        "unit": DEGREE
    },
    "dew": {
        "device": "weather", "name": "Dew Point",
        "device_class": SensorDeviceClass.TEMPERATURE,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfTemperature.CELSIUS
    },
    "heatindex": {
        "device": "weather", "name": "Heat Index",
        "device_class": SensorDeviceClass.TEMPERATURE,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfTemperature.CELSIUS
    },
    "hum": {
        "device": "weather", "name": "Humidity",
        "device_class": SensorDeviceClass.HUMIDITY,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": PERCENTAGE
    },
    "lastraintipiso": {
        "device": "weather", "name": "Last Rain Tip",
        "device_class": None,
        "state_class": None,
        "unit": None,
        "icon": "mdi:weather-rainy"
    },
    "temp": {
        "device": "weather", "name": "Temperature",
        "device_class": SensorDeviceClass.TEMPERATURE,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfTemperature.CELSIUS
    },
    "press": {
        "device": "weather", "name": "Pressure",
        "device_class": SensorDeviceClass.PRESSURE,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfPressure.HPA
    },
    "rfall": {
        "device": "weather", "name": "Rainfall",
        "device_class": SensorDeviceClass.PRECIPITATION,
        "state_class": SensorStateClass.TOTAL,
        "unit": UnitOfLength.MILLIMETERS
    },
    "rrate": {
        "device": "weather", "name": "Rainfall Rate",
        "device_class": SensorDeviceClass.PRECIPITATION_INTENSITY,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfVolumetricFlux.MILLIMETERS_PER_HOUR
    },
    "wgust": {
        "device": "weather", "name": "Wind Gust",
        "device_class": SensorDeviceClass.WIND_SPEED,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfSpeed.KILOMETERS_PER_HOUR
    },
    "wlatest": {
        "device": "weather", "name": "Wind Latest",
        "device_class": SensorDeviceClass.WIND_SPEED,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfSpeed.KILOMETERS_PER_HOUR
    },
    "wspeed": {
        "device": "weather", "name": "Wind Speed",
        "device_class": SensorDeviceClass.WIND_SPEED,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfSpeed.KILOMETERS_PER_HOUR
    },
    "wdir": {
        "device": "weather", "name": "Average Wind direction",
        "device_class": None,
        "state_class": None,
        "unit": None,
        "icon": "mdi:compass-outline"
    },
    "currentwdir": {
        "device": "weather", "name": "Wind Direction",
        "device_class": None,
        "state_class": None,
        "unit": None,
        "icon": "mdi:compass"
    },
}


def create_sensor_post_body(keys: str) -> dict:
    """
    Given a comma-separated string of keys, return a dictionary
    mapping each key to its CumulusMX tag template.
    Example: "temp, hum, dew" -> {"temp": "<#temp>", "hum": "<#hum>", "dew": "<#dew>"}
    """
    return {key.strip().lower(): f"<#{key.strip()}>" for key in keys.split(",") if key.strip()}
