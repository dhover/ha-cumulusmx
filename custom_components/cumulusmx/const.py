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
DEFAULT_WEBTAGS = [
    "temp",
    "hum",
    "dew",
    "heatindex",
    "press",
    "rfall",
    "rrate",
    "wgust",
    "wspeed",
    "wlatest",
    "wdir",
    "currentwdir",
    "bearing",
    "avgbearing",
    "LastRainTipISO",
    "ProgramUpTime",
    "SystemUpTime",
    "timehhmmss",
]
EXTRA_WEBTAGS = ["version","build","tempunit", "pressunit", "rainunit", "windunit"]
NON_SELECTABLE_WEBTAGS = set(EXTRA_WEBTAGS)

DEFAULT_UPDATE_INTERVAL = 60

# Endpoint for reading sensors
SENSOR_API_URL = "http://{host}:{port}/api/tags/process.txt"
GITHUB_API_URL = "https://api.github.com/repos/cumulusmx/cumulusmx/releases/latest"

SENSOR_TYPES = {
    # Sensors for Airlink device
    "AirLinkPm1Out": {
        "device": "airlink", "name": "PM 1.0",
        "device_class": SensorDeviceClass.PM1,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
    },
    "AirLinkPm2p5Out": {
        "device": "airlink", "name": "PM 2.5",
        "device_class": SensorDeviceClass.PM25,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
    },
    "AirLinkPm2p5_1hrOut": {
        "device": "airlink", "name": "PM 2.5 1h",
        "device_class": SensorDeviceClass.PM25,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
    },
    "AirLinkPm2p5_3hrOut": {
        "device": "airlink", "name": "PM 2.5 3h",
        "device_class": SensorDeviceClass.PM25,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
    },
    "AirLinkPm2p5_24hrOut": {
        "device": "airlink", "name": "PM 2.5 24h",
        "device_class": SensorDeviceClass.PM25,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
    },
    "AirLinkPm2p5_NowcastOut": {
        "device": "airlink", "name": "Pm 2.5 Nowcast",
        "device_class": SensorDeviceClass.PM25,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
    },
    "AirLinkPm10Out": {
        "device": "airlink", "name": "PM 10",
        "device_class": SensorDeviceClass.PM10,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
    },
    "AirLinkPm10_1hrOut": {
        "device": "airlink", "name": "PM 10 1h",
        "device_class": SensorDeviceClass.PM10,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
    },
    "AirLinkPm10_3hrOut": {
        "device": "airlink", "name": "PM 10 3h",
        "device_class": SensorDeviceClass.PM10,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
    },
    "AirLinkPm10_24hrOut": {
        "device": "airlink", "name": "PM 10 24h",
        "device_class": SensorDeviceClass.PM10,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
    },
    "AirLinkPm10_NowcastOut": {
        "device": "airlink", "name": "PM 10 Nowcast",
        "device_class": SensorDeviceClass.PM10,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": CONCENTRATION_MICROGRAMS_PER_CUBIC_METER
    },
    "AirLinkAqiPm2p5Out": {
        "device": "airlink", "name": "PM 2.5 AQI",
        "device_class": SensorDeviceClass.AQI,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": None
    },
    "AirLinkAqiPm2p5_1hrOut": {
        "device": "airlink", "name": "PM 2.5 AQI 1h",
        "device_class": SensorDeviceClass.AQI,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": None
    },
    "AirLinkAqiPm2p5_3hrOut": {
        "device": "airlink", "name": "PM 2.5 AQI 3h",
        "device_class": SensorDeviceClass.AQI,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": None
    },
    "AirLinkAqiPm2p5_24hrOut": {
        "device": "airlink", "name": "PM 2.5 AQI 24h",
        "device_class": SensorDeviceClass.AQI,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": None
    },
    "AirLinkAqiPm2p5_NowcastOut": {
        "device": "airlink", "name": "PM 2.5 AQI Nowcast",
        "device_class": SensorDeviceClass.AQI,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": None
    },
    "AirLinkAqiPm10Out": {
        "device": "airlink", "name": "PM 10 AQI",
        "device_class": SensorDeviceClass.AQI,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": None
    },
    "AirLinkAqiPm10_1hrOut": {
        "device": "airlink", "name": "PM 10 AQI 1h",
        "device_class": SensorDeviceClass.AQI,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": None
    },
    "AirLinkAqiPm10_3hrOut": {
        "device": "airlink", "name": "PM 10 AQI 3h",
        "device_class": SensorDeviceClass.AQI,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": None
    },
    "AirLinkAqiPm10_24hrOut": {
        "device": "airlink", "name": "PM 10 AQI 24h",
        "device_class": SensorDeviceClass.AQI,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": None
    },
    "AirLinkAqiPm10_NowcastOut": {
        "device": "airlink", "name": "PM 10 AQI Nowcast",
        "device_class": SensorDeviceClass.AQI,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": None
    },
    "AirLinkHumOut": {
        "device": "airlink", "name": "Humidity",
        "device_class": SensorDeviceClass.HUMIDITY,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": PERCENTAGE
    },
    "AirLinkTempOut": {
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
    "MulticastBadCnt": {
        "device": "system", "name": "Bad packets",
        "device_class": None,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "unit": None,
        "icon": "mdi:alert"
    },
    "MulticastGoodCnt": {
        "device": "system", "name": "Good packets",
        "device_class": None,
        "state_class": SensorStateClass.TOTAL_INCREASING,
        "unit": None,
        "icon": "mdi:check-circle"
    },
    "MulticastGoodPct": {
        "device": "system", "name": "Good packets percent",
        "device_class": None,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": PERCENTAGE,
        "icon": "mdi:percent"
    },
    "ProgramUpTime": {
        "device": "system", "name": "Uptime",
        "device_class": None,
        "state_class": None,
        "unit": None,
        "icon": "mdi:clock-outline"
    },
    "SystemUpTime": {
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
    "txbattery channel=1": {
        "device": "system", "name": "Battery ISS 1",
        "device_class": None,
        "state_class": None,
        "unit": None,
        "icon": "mdi:battery-outline"
    },
    "txbattery channel=2": {
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
    "LastRainTipISO": {
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
    "intemp": {
        "device": "weather", "name": "Indoor Temperature",
        "device_class": SensorDeviceClass.TEMPERATURE,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": UnitOfTemperature.CELSIUS,
    },
    "inhum": {
        "device": "weather", "name": "Indoor Humidity",
        "device_class": SensorDeviceClass.HUMIDITY,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": PERCENTAGE,
    },
    "SolarRad": {
        "device": "weather", "name": "Solar Radiation",
        "device_class": SensorDeviceClass.IRRADIANCE,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": None,
    },
    "UV": {
        "device": "weather", "name": "UV Index",
        "device_class": "",
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": None,
    },
}

# Complete list of known webtags for selector choices.
ALL_WEBTAG_OPTIONS = []
_webtag_options_seen = set()
for _webtag in [*DEFAULT_WEBTAGS, *SENSOR_TYPES.keys()]:
    if _webtag in NON_SELECTABLE_WEBTAGS:
        continue
    if _webtag in _webtag_options_seen:
        continue
    _webtag_options_seen.add(_webtag)
    ALL_WEBTAG_OPTIONS.append(_webtag)


def normalize_webtags(webtags) -> list[str]:
    """Normalize webtags from either a CSV string or a list into a deduped list."""
    if not webtags:
        return []
    if isinstance(webtags, str):
        items = [item.strip() for item in webtags.split(",")]
    elif isinstance(webtags, (list, tuple, set)):
        items = [str(item).strip() for item in webtags]
    else:
        return []

    normalized = []
    seen = set()
    for item in items:
        if not item:
            continue
        if item not in seen:
            normalized.append(item)
            seen.add(item)
    return normalized


def normalize_configurable_webtags(webtags) -> list[str]:
    """Normalize user-configurable webtags and remove always-added tags."""
    return [
        tag for tag in normalize_webtags(webtags)
        if tag not in NON_SELECTABLE_WEBTAGS
    ]


def create_sensor_post_body(keys) -> dict:
    """
    Given a list or comma-separated string of keys, return a dictionary
    mapping each key to its CumulusMX tag template.
    Example: ["temp", "hum", "dew"] -> {"temp": "<#temp>", "hum": "<#hum>", "dew": "<#dew>"}
    """
    return {
        key.strip(): f"<#{key.strip()}>"
        for key in normalize_webtags(keys)
    }
