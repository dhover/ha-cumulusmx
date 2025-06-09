from homeassistant.const import (
    UnitOfTemperature,
    UnitOfPressure,
    UnitOfLength,
    UnitOfSpeed,
    CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    PERCENTAGE,
    UnitOfTime,
)

# Constants for CumulusMX integration

DOMAIN = "cumulusmx"

CONF_UPDATE_INTERVAL = "update_interval"
CONF_HOST = "host"
CONF_PORT = "port"
CONF_WEBTAGS = "webtags"

DEFAULT_HOST = "192.168.x.x"
DEFAULT_PORT = 8998
DEFAULT_WEBTAGS = "temp,hum,dew,press,rfall,rrate,wgust,wspeed,wlatest,bearing,avgbearing,LastRainTipISO,AirLinkPm1Out,AirLinkPm2p5Out,AirLinkPm2p5_1hrOut,AirLinkPm2p5_3hrOut,AirLinkPm2p5_24hrOut,AirLinkPm2p5_NowcastOut,AirLinkPm10Out,AirLinkPm10_1hrOut,AirLinkPm10_3hrOut,AirLinkPm10_24hrOut,AirLinkPm10_NowcastOut,AirLinkAqiPm2p5Out,AirLinkAqiPm2p5_1hrOut,AirLinkAqiPm2p5_3hrOut,AirLinkAqiPm2p5_24hrOut,AirLinkAqiPm2p5_NowcastOut,AirLinkAqiPm10Out,AirLinkAqiPm10_1hrOut,AirLinkAqiPm10_3hrOut,AirLinkAqiPm10_24hrOut,AirLinkAqiPm10_NowcastOut,AirLinkTempOut,AirLinkHumOut,MulticastGoodCnt,MulticastBadCnt,MulticastGoodPct,ProgramUpTime,SystemUpTime,version,build,timehhmmss"
DEFAULT_UPDATE_INTERVAL = 60

# Endpoint for reading sensors
SENSOR_API_URL = "http://{host}:{port}/api/tags/process.txt"

SENSOR_TYPES = {
    # Sensors for Airlink device
    "airlinkpm1out": {"device": "airlink", "name": "PM 1.0", "device_class": "PM1", "state_class": "measurement", "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER},
    "airlinkpm2p5out": {"device": "airlink", "name": "PM 2.5", "device_class": "PM25", "state_class": "measurement", "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER},
    "airlinkpm2p5_1hrout": {"device": "airlink", "name": "PM 2.5 1h", "device_class": "PM25", "state_class": "measurement", "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER},
    "airlinkpm2p5_3hrout": {"device": "airlink", "name": "PM 2.5 3h", "device_class": "PM25", "state_class": "measurement", "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER},
    "airlinkpm2p5_24hrout": {"device": "airlink", "name": "PM 2.5 24h", "device_class": "PM25", "state_class": "measurement", "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER},
    "airlinkpm2p5_nowcastout": {"device": "airlink", "name": "Pm 2.5 Nowcast", "device_class": "PM25", "state_class": "measurement", "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER},
    "airlinkpm10out": {"device": "airlink", "name": "PM 10", "device_class": "PM10", "state_class": "measurement", "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER},
    "airlinkpm10_1hrout": {"device": "airlink", "name": "PM 10 1h", "device_class": "PM10", "state_class": "measurement", "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER},
    "airlinkpm10_3hrout": {"device": "airlink", "name": "PM 10 3h", "device_class": "PM10", "state_class": "measurement", "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER},
    "airlinkpm10_24hrout": {"device": "airlink", "name": "PM 10 24h", "device_class": "PM10", "state_class": "measurement", "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER},
    "airlinkpm10_nowcastout": {"device": "airlink", "name": "PM 10 Nowcast", "device_class": "PM10", "state_class": "measurement", "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER},
    "airlinkaqipm2p5out": {"device": "airlink", "name": "PM 2.5 AQI", "device_class": None, "state_class": "measurement", "unit": None},
    "airlinkaqipm2p5_1hrout": {"device": "airlink", "name": "PM 2.5 AQI 1h", "device_class": None, "state_class": "measurement", "unit": None},
    "airlinkaqipm2p5_3hrout": {"device": "airlink", "name": "PM 2.5 AQI 3h", "device_class": None, "state_class": "measurement", "unit": None},
    "airlinkaqipm2p5_24hrout": {"device": "airlink", "name": "PM 2.5 AQI 24h", "device_class": None, "state_class": "measurement", "unit": None},
    "airlinkaqipm2p5_nowcastout": {"device": "airlink", "name": "PM 2.5 AQI Nowcast", "device_class": None, "state_class": "measurement", "unit": None},
    "airlinkaqipm10out": {"device": "airlink", "name": "PM 10 AQI", "device_class": None, "state_class": "measurement", "unit": None},
    "airlinkaqipm10_1hrout": {"device": "airlink", "name": "PM 10 AQI 1h", "device_class": None, "state_class": "measurement", "unit": None},
    "airlinkaqipm10_3hrout": {"device": "airlink", "name": "PM 10 AQI 3h", "device_class": None, "state_class": "measurement", "unit": None},
    "airlinkaqipm10_24hrout": {"device": "airlink", "name": "PM 10 AQL 24h", "device_class": None, "state_class": "measurement", "unit": None},
    "airlinkaqipm10_nowcastout": {"device": "airlink", "name": "PM 10 AQI Nowcast", "device_class": None, "state_class": "measurement", "unit": None},
    "airlinktempout": {"device": "airlink", "name": "Temperature", "device_class": "temperature", "state_class": "measurement", "unit": UnitOfTemperature.CELSIUS},
    "airlinkhumout": {"device": "airlink", "name": "Humidity", "device_class": "humidity", "state_class": "measurement", "unit": PERCENTAGE},
    # Sensors for System Info device
    "timehhmmss": {"device": "system", "name": "Time", "device_class": None, "state_class": "None", "unit": None},
    "multicastgoodcnt": {"device": "system", "name": "Good packets", "device_class": None, "state_class": "total_increasing", "unit": None},
    "multicastbadcnt": {"device": "system", "name": "Bad packets", "device_class": None, "state_class": "total_increasing", "unit": None},
    "multicastgoodpct": {"device": "system", "name": "Good packets percent", "device_class": None, "state_class": "measurement", "unit": PERCENTAGE},
    "programuptime": {"device": "system", "name": "Uptime", "device_class": None, "state_class": None, "unit": None},
    "systemuptime": {"device": "system", "name": "System Uptime", "device_class": None, "state_class": None, "unit": None},
    "version": {"device": "system", "name": "Version", "device_class": None, "state_class": None, "unit": None},
    "build": {"device": "system", "name": "Build", "device_class": None, "state_class": None, "unit": None},
    # Sensors for Weather device (the rest)
    "temp": {"device": "weather", "name": "Temperature", "device_class": "temperature", "state_class": "measurement", "unit": UnitOfTemperature.CELSIUS},
    "hum": {"device": "weather", "name": "Humidity", "device_class": "humidity", "state_class": "measurement", "unit": PERCENTAGE},
    "press": {"device": "weather", "name": "Pressure", "device_class": "pressure", "state_class": "measurement", "unit": UnitOfPressure.HPA},
    "rfall": {"device": "weather", "name": "Rainfall", "device_class": None, "state_class": "total_increasing", "unit": UnitOfLength.MILLIMETERS},
    "rrate": {"device": "weather", "name": "Rainfall Rate", "device_class": None, "state_class": "measurement", "unit": f"{UnitOfLength.MILLIMETERS}/h"},
    "dew": {"device": "weather", "name": "Dew Point", "device_class": "temperature", "state_class": "measurement", "unit": UnitOfTemperature.CELSIUS},
    "wgust": {"device": "weather", "name": "Wind Gust", "device_class": None, "state_class": "measurement", "unit": UnitOfSpeed.KILOMETERS_PER_HOUR},
    "wspeed": {"device": "weather", "name": "Wind Speed", "device_class": None, "state_class": "measurement", "unit": UnitOfSpeed.KILOMETERS_PER_HOUR},
    "wlatest": {"device": "weather", "name": "Wind Latest", "device_class": None, "state_class": "measurement", "unit": UnitOfSpeed.KILOMETERS_PER_HOUR},
    "bearing": {"device": "weather", "name": "Bearing", "device_class": None, "state_class": "measurement", "unit": "°"},
    "avgbearing": {"device": "weather", "name": "Average Bearing", "device_class": None, "state_class": "measurement", "unit": "°"},
    "lastraintipiso": {"device": "weather", "name": "Last Rain Tip", "device_class": None, "state_class": None, "unit": None},
}


def create_sensor_post_body(keys: str) -> dict:
    """
    Given a comma-separated string of keys, return a dictionary
    mapping each key to its CumulusMX tag template.
    Example: "temp, hum, dew" -> {"temp": "<#temp rc=y>", "hum": "<#hum rc=y>", "dew": "<#dew rc=y>"}
    """
    return {key.strip().lower(): f"<#{key.strip()}>" for key in keys.split(",") if key.strip()}
