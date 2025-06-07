from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import Entity
from homeassistant.const import CONF_NAME, CONF_UNIT_OF_MEASUREMENT
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import SENSOR_TYPES, SENSOR_TYPES_AIRLINK, SENSOR_TYPES_SYSTEM
from .coordinator import CumulusMXCoordinator

UNIT_KEYS = {"tempunit", "humunit", "pressunit",
             "rainunit", "rrateunit", "windunit"}

# Device info definitions


def get_device_info(device_type, host, port):
    if device_type == "airlink":
        return {
            "identifiers": {("cumulusmx", "airlink")},
            "name": "Davis Airlink",
            "manufacturer": "CumulusMX",
            "model": "Airlink",
            "configuration_url": f"http://{host}:{port}"
        }
    elif device_type == "system":
        return {
            "identifiers": {("cumulusmx", "system")},
            "name": "CumulusMX System Info",
            "manufacturer": "CumulusMX",
            "model": "System",
            "configuration_url": f"http://{host}:{port}"
        }
    else:
        return {
            "identifiers": {("cumulusmx", "weather")},
            "name": "Davis Vantage Pro 2",
            "manufacturer": "Davis",
            "model": "Vantage Pro 2",
            "configuration_url": f"http://{host}:{port}"
        }


def get_device_type(key):
    # Use airlink device type if the key is in SENSOR_TYPES_AIRLINK
    if key in SENSOR_TYPES_AIRLINK:
        return "airlink"
    # System sensors (packets, uptime, version, build)
    if key in SENSOR_TYPES_SYSTEM:
        return "system"
    # All others are weather sensors
    return "weather"


async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator = hass.data["cumulusmx"][config_entry.entry_id]
    sensors = []
    for key, sensor_info in SENSOR_TYPES.items():
        # if key not in UNIT_KEYS:
        device_type = get_device_type(key)
        sensors.append(CumulusMXSensor(
            coordinator, key, sensor_info, device_type))
    async_add_entities(sensors)


class CumulusMXSensor(CoordinatorEntity, SensorEntity):
    _attr_has_entity_name = True

    def __init__(self, coordinator: CumulusMXCoordinator, key: str, sensor_info: dict, device_type: str):
        super().__init__(coordinator)
        self._key = key
        self._sensor_info = sensor_info
        self._device_type = device_type
        self._host = coordinator.host
        self._port = coordinator.port
        self._attr_state_class = sensor_info.get("state_class")

    @property
    def name(self):
        return self._sensor_info.get("name", self._key)

    @property
    def state(self):
        value = self.coordinator.data.get(
            self._key) if self.coordinator.data else None
        # Replace comma by dot for goodpacketspercent
        if self._key == "goodpacketspercent" and isinstance(value, str):
            return value.replace(",", ".")
        return value

    @property
    def unique_id(self):
        return f"cumulusmx_{self._key}"

    @property
    def unit_of_measurement(self):
        if self._key in {"temp", "dew", "airlinktempout"}:
            return self.coordinator.data.get("tempunit", "").replace("&#176;", "°") if self.coordinator.data else None
        if self._key in {"press"}:
            return self.coordinator.data.get("pressunit") if self.coordinator.data else None
        if self._key in {"hum", "airlinkhumout"}:
            return self.coordinator.data.get("humunit") if self.coordinator.data else None
        if self._key in {"wgust", "wspeed", "wlatest"}:
            return self.coordinator.data.get("windunit") if self.coordinator.data else None
        if self._key in {"rfall"}:
            return self.coordinator.data.get("rainunit") if self.coordinator.data else None
        if self._key in {"rrate"}:
            return self.coordinator.data.get("rrateunit") if self.coordinator.data else None
        if self._key in {"pm1", "pm2p5", "pm2p5_1hr", "pm2p5_3hr", "pm2p5_24hr", "pm2p5_nowcast",
                         "pm10", "pm10_1hr", "pm10_3hr", "pm10_24hr", "pm10_nowcast"}:
            return "µg/m³"
        if self._key in {"bearing", "avgbearing"}:
            return "°"
        return None

    @property
    def device_class(self):
        return self._sensor_info.get("device_class")

    # @property
    # def state_class(self):
    #    return self._sensor_info.get("state_class")

    @property
    def device_info(self):
        return get_device_info(self._device_type, self._host, self._port)
