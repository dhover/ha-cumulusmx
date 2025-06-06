# Constants for CumulusMX integration

DOMAIN = "cumulusmx"

CONF_UPDATE_INTERVAL = "update_interval"
CONF_HOST = "host"
CONF_PORT = "8998"

DEFAULT_UPDATE_INTERVAL = 60  # in seconds

# Endpoint for reading sensors
SENSOR_API_URL = "http://{host}:{port}/api/tags/process.txt"

# Sensors for Airlink device
SENSOR_TYPES_AIRLINK = {
    "pm1": {"name": "PM 1.0", "device_class": "PM1", "state_class": "measurement"},
    "pm2p5": {"name": "PM 2.5", "device_class": "PM25", "state_class": "measurement"},
    "pm2p5_1hr": {"name": "PM 2.5 1h", "device_class": "PM25", "state_class": "measurement"},
    "pm2p5_3hr": {"name": "PM 2.5 3h", "device_class": "PM25", "state_class": "measurement"},
    "pm2p5_24hr": {"name": "PM 2.5 24h", "device_class": "PM25", "state_class": "measurement"},
    "pm2p5_nowcast": {"name": "Pm 2.5 Nowcast", "device_class": "PM25", "state_class": "measurement"},
    "pm10": {"name": "PM 10", "device_class": "PM10", "state_class": "measurement"},
    "pm10_1hr": {"name": "PM 10 1h", "device_class": "PM10", "state_class": "measurement"},
    "pm10_3hr": {"name": "PM 10 3h", "device_class": "PM10", "state_class": "measurement"},
    "pm10_24hr": {"name": "PM 10 24h", "device_class": "PM10", "state_class": "measurement"},
    "pm10_nowcast": {"name": "PM 10 Nowcast", "device_class": "PM10", "state_class": "measurement"},
    "pm2p5_aqi": {"name": "PM 2.5 AQI", "device_class": None, "state_class": "measurement"},
    "pm2p5_aqi_1hr": {"name": "PM 2.5 AQI 1h", "device_class": None, "state_class": "measurement"},
    "pm2p5_aqi_3hr": {"name": "PM 2.5 AQI 3h", "device_class": None, "state_class": "measurement"},
    "pm2p5_aqi_24hr": {"name": "PM 2.5 AQI 24h", "device_class": None, "state_class": "measurement"},
    "pm2p5_aqi_nowcast": {"name": "PM 2.5 AQI Nowcast", "device_class": None, "state_class": "measurement"},
    "pm10_aqi": {"name": "PM 10 AQI", "device_class": None, "state_class": "measurement"},
    "pm10_aqi_1hr": {"name": "PM 10 AQI 1h", "device_class": None, "state_class": "measurement"},
    "pm10_aqi_3hr": {"name": "PM 10 AQI 3h", "device_class": None, "state_class": "measurement"},
    "pm10_aqi_24hr": {"name": "PM 10 AQL 24h", "device_class": None, "state_class": "measurement"},
    "pm10_aqi_nowcast": {"name": "PM 10 AQI Nowcast", "device_class": None, "state_class": "measurement"},
    "airlinktempout": {"name": "Temperature", "device_class": "temperature", "state_class": "measurement"},
    "airlinkhumout": {"name": "Humidity", "device_class": "humidity", "state_class": "measurement"},
}

# Sensors for System Info device
SENSOR_TYPES_SYSTEM = {
    "goodpackets": {"name": "Good packets", "device_class": None, "state_class": "total_increasing"},
    "badpackets": {"name": "Bad packets", "device_class": None, "state_class": "total_increasing"},
    "goodpacketspercent": {"name": "Good packets percent", "device_class": None, "state_class": "measurement"},
    "uptime": {"name": "Uptime", "device_class": None, "state_class": None},
    "systemuptime": {"name": "System Uptime", "device_class": None, "state_class": None},
    "version": {"name": "Version", "device_class": None, "state_class": None},
    "build": {"name": "Build", "device_class": None, "state_class": None},
}

# Sensors for Weather device (the rest)
SENSOR_TYPES_WEATHER = {
    "temp": {"name": "Temperature", "device_class": "temperature", "state_class": "measurement"},
    "hum": {"name": "Humidity", "device_class": "humidity", "state_class": "measurement"},
    "press": {"name": "Pressure", "device_class": "pressure", "state_class": "measurement"},
    "rfall": {"name": "Rainfall", "device_class": None, "state_class": "total_increasing"},
    "rrate": {"name": "Rainfall Rate", "device_class": None, "state_class": "measurement"},
    "wgust": {"name": "Wind Gust", "device_class": None, "state_class": "measurement"},
    "wspeed": {"name": "Wind Speed", "device_class": None, "state_class": "measurement"},
    "wlatest": {"name": "Wind Latest", "device_class": None, "state_class": "measurement"},
    "bearing": {"name": "Bearing", "device_class": None, "state_class": "measurement"},
    "avgbearing": {"name": "Average Bearing", "device_class": None, "state_class": "measurement"},
    "lastraintipiso": {"name": "Last Rain Tip", "device_class": None, "state_class": None},
    "dew": {"name": "Dew Point", "device_class": "temperature", "state_class": "measurement"},
    "time": {"name": "Time", "device_class": None, "state_class": None},
}

# Units for sensors
SENSOR_UNITS = {
    "tempunit": {"name": "Temperature Unit", "device_class": None, "state_class": None},
    "humunit": {"name": "Humidity Unit", "device_class": None, "state_class": None},
    "pressunit": {"name": "Pressure Unit", "device_class": None, "state_class": None},
    "rainunit": {"name": "Rainfall Unit", "device_class": None, "state_class": None},
    "rrateunit": {"name": "Rain Rate Unit", "device_class": None, "state_class": None},
    "windunit": {"name": "Wind Speed Unit", "device_class": None, "state_class": None},
}

# For backward compatibility, you can merge all if needed
SENSOR_TYPES = {
    **SENSOR_TYPES_AIRLINK,
    **SENSOR_TYPES_SYSTEM,
    **SENSOR_TYPES_WEATHER,
    # **SENSOR_UNITS,
}

SENSOR_POST_BODY = """
{
"time":"<#year rc=y>-<#month rc=y>-<#day rc=y> <#timehhmmss rc=y>",
"temp":"<#temp rc=y>",
"hum":"<#hum rc=y>",
"press":"<#press rc=y>",
"rfall":"<#rfall rc=y>",
"rrate":"<#rrate rc=y>",
"wgust":"<#wgust rc=y>",
"wspeed":"<#wspeed rc=y>",
"wlatest":"<#wlatest rc=y>",
"bearing":"<#bearing rc=y>",
"avgbearing":"<#avgbearing rc=y>",
"lastraintipiso":"<#LastRainTipISO rc=y>",
"dew":"<#dew rc=y>",
"pm1":"<#AirLinkPm1Out rc=y>",
"pm2p5":"<#AirLinkPm2p5Out rc=y>",
"pm2p5_1hr":"<#AirLinkPm2p5_1hrOut rc=y>",
"pm2p5_3hr":"<#AirLinkPm2p5_3hrOut rc=y>",
"pm2p5_24hr":"<#AirLinkPm2p5_24hrOut rc=y>",
"pm2p5_nowcast":"<#AirLinkPm2p5_NowcastOut rc=y>",
"pm10":"<#AirLinkPm10Out rc=y>",
"pm10_1hr":"<#AirLinkPm10_1hrOut rc=y>",
"pm10_3hr":"<#AirLinkPm10_3hrOut rc=y>",
"pm10_24hr":"<#AirLinkPm10_24hrOut rc=y>",
"pm10_nowcast":"<#AirLinkPm10_NowcastOut rc=y>",
"pm2p5_aqi":"<#AirLinkAqiPm2p5Out rc=y>",
"pm2p5_aqi_1hr":"<#AirLinkAqiPm2p5_1hrOut rc=y>",
"pm2p5_aqi_3hr":"<#AirLinkAqiPm2p5_3hrOut rc=y>",
"pm2p5_aqi_24hr":"<#AirLinkAqiPm2p5_24hrOut rc=y>",
"pm2p5_aqi_nowcast":"<#AirLinkAqiPm2p5_NowcastOut rc=y>",
"pm10_aqi":"<#AirLinkAqiPm10Out rc=y>",
"pm10_aqi_1hr":"<#AirLinkAqiPm10_1hrOut rc=y>",
"pm10_aqi_3hr":"<#AirLinkAqiPm10_3hrOut rc=y>",
"pm10_aqi_24hr":"<#AirLinkAqiPm10_24hrOut rc=y>",
"pm10_aqi_nowcast":"<#AirLinkAqiPm10_NowcastOut rc=y>",
"airlinktempout":"<#AirLinkTempOut rc=y>",
"airlinkhumout":"<#AirLinkHumOut rc=y>",
"goodpackets":"<#MulticastGoodCnt rc=y>",
"badpackets":"<#MulticastBadCnt rc=y>",
"goodpacketspercent":"<#MulticastGoodPct rc=y>",
"uptime":"<#ProgramUpTime rc=y>",
"systemuptime":"<#SystemUpTime rc=y>",
"version":"<#version rc=y>",
"build":"<#build rc=y>",
"tempunit":"<#tempunit rc=y>",
"humunit":"%",
"pressunit":"<#pressunit rc=y>",
"rainunit":"<#rainunit rc=y>",
"rrateunit":"<#rainunit rc=y>/h",
"windunit":"<#windunit rc=y>"
}
"""
