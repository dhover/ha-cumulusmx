"""Platform for sensor integration."""

import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.const import (
    UnitOfTemperature,
    UnitOfPressure,
    UnitOfPrecipitationDepth,
    UnitOfVolumetricFlux,
    UnitOfSpeed
)

from .const import SENSOR_TYPES
from .coordinator import CumulusMXCoordinator

_LOGGER = logging.getLogger(__name__)

# Device info definitions


def get_device_info(device_type, host, port):
    """Return device info based on device type."""

    if device_type == "airlink":
        return {
            "identifiers": {("cumulusmx", "airlink")},
            "name": "Davis Airlink",
            "manufacturer": "Davis",
            "model": "Airlink",
            "configuration_url": f"http://{host}:{port}"
        }
    elif device_type == "system":
        return {
            "identifiers": {("cumulusmx", "system")},
            "name": "CumulusMX System Info",
            "manufacturer": "CumulusMX",
            "model": "System Info",
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
    """Return device type based on sensor key."""

    # Use airlink device type if the key is in SENSOR_TYPES_AIRLINK
    if key in SENSOR_TYPES:
        device_type = SENSOR_TYPES.get(key, {}).get("device", "weather")
        return device_type
    return None


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up sensors based on a config entry."""

    coordinator = hass.data["cumulusmx"][config_entry.entry_id]
    sensors = []
    # Wait for the first data refresh to get all keys
    await coordinator.async_refresh()
    if not coordinator.data:
        return

    temp_unit = coordinator.data["tempunit"]
    press_unit = coordinator.data["pressunit"]
    rain_unit = coordinator.data["rainunit"]
    wind_unit = coordinator.data["windunit"]
    _LOGGER.warning("temp_unit: %s", temp_unit)
    _LOGGER.warning("press_unit: %s", press_unit)
    _LOGGER.warning("rain_unit: %s", rain_unit)
    _LOGGER.warning("wind_unit: %s", wind_unit)

    for key in coordinator.data.keys():
        sensor_info = SENSOR_TYPES.get(key, {
            "name": key.replace("_", " ").title(),
            "device": None,
            "device_class": None,
            "state_class": None,
            "unit": None,
            "icon": None
        }).copy()

        if sensor_info["device_class"] == SensorDeviceClass.TEMPERATURE:
            match temp_unit:
                case "&#176;C":
                    sensor_info["unit"] = UnitOfTemperature.CELSIUS
                case "&#176;F":
                    sensor_info["unit"] = UnitOfTemperature.FAHRENHEIT

        if sensor_info["device_class"] == SensorDeviceClass.PRESSURE:
            match press_unit:
                case "hPa":
                    sensor_info["unit"] = UnitOfPressure.HPA
                case "kPa":
                    sensor_info["unit"] = UnitOfPressure.KPA
                case "mb":
                    sensor_info["unit"] = UnitOfPressure.MBAR
                case "in":
                    sensor_info["unit"] = UnitOfPressure.INHG

        if sensor_info["device_class"] == SensorDeviceClass.PRECIPITATION:
            match rain_unit:
                case "mm":
                    sensor_info["unit"] = UnitOfPrecipitationDepth.MILLIMETERS
                case "inches":
                    sensor_info["unit"] = UnitOfPrecipitationDepth.INCHES

        if sensor_info["device_class"] == SensorDeviceClass.PRECIPITATION_INTENSITY:
            match rain_unit:
                case "mm":
                    sensor_info["unit"] = UnitOfVolumetricFlux.MILLIMETERS_PER_HOUR
                case "inches":
                    sensor_info["unit"] = UnitOfVolumetricFlux.INCHES_PER_HOUR

        if sensor_info["device_class"] == SensorDeviceClass.WIND_SPEED:
            match wind_unit:
                case "m/s":
                    sensor_info["unit"] = UnitOfSpeed.METERS_PER_SECOND
                case "mph":
                    sensor_info["unit"] = UnitOfSpeed.MILES_PER_HOUR
                case "km/h":
                    sensor_info["unit"] = UnitOfSpeed.KILOMETERS_PER_HOUR
                case "kts":
                    sensor_info["unit"] = UnitOfSpeed.KNOTS

        device_type = get_device_type(key)
        if device_type is not None:
            sensors.append(CumulusMXSensor(
                coordinator, key, sensor_info, device_type))
    async_add_entities(sensors)


class CumulusMXSensor(CoordinatorEntity, SensorEntity):
    """Representation of a CumulusMX sensor."""

    _attr_has_entity_name = True

    def __init__(self, coordinator: CumulusMXCoordinator, key: str,
                    sensor_info: dict, device_type: str):
        super().__init__(coordinator)
        self._key = key
        self._sensor_info = sensor_info
        self._device_type = device_type
        self._host = coordinator.host
        self._port = coordinator.port

    @property
    def name(self):
        """Return the name of the sensor."""    
        return self._sensor_info.get("name", self._key)

    @property
    def state(self):
        """Return the state of the sensor."""
        value = self.coordinator.data.get(
            self._key) if self.coordinator.data else None
        # Replace comma by dot if value is numeric and contains a comma
        if isinstance(value, str) and "," in value:
            try:
                # Try converting to float after replacing comma
                float(value.replace(",", "."))
                return value.replace(",", ".")
            except ValueError:
                pass
        return value

    @property
    def unique_id(self):
        """Return a unique ID."""
        # Voeg device_type en host toe voor extra uniekheid
        return f"cumulusmx_{self._device_type}_{self._key}"

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        # Prefer dynamic unit from coordinator.data if available and not None
        dynamic_unit = self.coordinator.data.get(
            f"{self._key}unit") if self.coordinator.data else None
        if dynamic_unit:
            return dynamic_unit.replace("&#176;", "°")
        # Otherwise, use the static unit from SENSOR_TYPES
        return self._sensor_info.get("unit")

    @property
    def device_class(self):
        """Return the device class."""
        return self._sensor_info.get("device_class")

    @property
    def state_class(self):
        """Return the state class."""
        return self._sensor_info.get("state_class")

    @property
    def device_info(self):
        """Return device information."""
        return get_device_info(self._device_type, self._host, self._port)

    @property
    def icon(self):
        """Return the icon if set and no icon device_class is defined, otherwise None"""
        if self._sensor_info.get("icon"):
            return self._sensor_info["icon"]
        return None
