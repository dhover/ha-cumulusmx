"""Unit tests for custom_components.cumulusmx.sensor."""

from __future__ import annotations

from dataclasses import dataclass
import importlib.util
from pathlib import Path
import sys
import types
import unittest
from types import SimpleNamespace


def _load_sensor_module():
    """Load the sensor module with lightweight Home Assistant stubs."""
    sensor_path = (
        Path(__file__).resolve().parents[1]
        / "custom_components"
        / "cumulusmx"
        / "sensor.py"
    )

    for module_name in (
        "custom_components.cumulusmx.sensor",
        "custom_components.cumulusmx.const",
        "custom_components.cumulusmx.coordinator",
        "custom_components.cumulusmx",
        "custom_components",
        "homeassistant",
        "homeassistant.components",
        "homeassistant.components.sensor",
        "homeassistant.helpers",
        "homeassistant.helpers.entity",
        "homeassistant.helpers.update_coordinator",
        "homeassistant.const",
    ):
        sys.modules.pop(module_name, None)

    custom_components = types.ModuleType("custom_components")
    custom_components.__path__ = [str(sensor_path.parents[1])]
    sys.modules["custom_components"] = custom_components

    cumulusmx_pkg = types.ModuleType("custom_components.cumulusmx")
    cumulusmx_pkg.__path__ = [str(sensor_path.parent)]
    sys.modules["custom_components.cumulusmx"] = cumulusmx_pkg

    homeassistant = types.ModuleType("homeassistant")
    sys.modules["homeassistant"] = homeassistant

    ha_components = types.ModuleType("homeassistant.components")
    sys.modules["homeassistant.components"] = ha_components

    ha_sensor = types.ModuleType("homeassistant.components.sensor")

    class SensorEntity:
        """Minimal sensor entity stub."""

    class SensorDeviceClass:
        TEMPERATURE = "temperature"
        PRESSURE = "pressure"
        PRECIPITATION = "precipitation"
        PRECIPITATION_INTENSITY = "precipitation_intensity"
        WIND_SPEED = "wind_speed"
        ENUM = "enum"

    ha_sensor.SensorEntity = SensorEntity
    ha_sensor.SensorDeviceClass = SensorDeviceClass
    sys.modules["homeassistant.components.sensor"] = ha_sensor

    ha_helpers = types.ModuleType("homeassistant.helpers")
    sys.modules["homeassistant.helpers"] = ha_helpers

    ha_entity = types.ModuleType("homeassistant.helpers.entity")

    @dataclass(eq=True)
    class DeviceInfo:
        """Minimal device info stub."""

        identifiers: set | None = None
        translation_key: str | None = None
        translation_placeholders: dict | None = None
        manufacturer: str | None = None
        model: str | None = None
        configuration_url: str | None = None
        via_device: tuple | None = None

    ha_entity.DeviceInfo = DeviceInfo
    sys.modules["homeassistant.helpers.entity"] = ha_entity

    ha_update_coordinator = types.ModuleType(
        "homeassistant.helpers.update_coordinator"
    )

    class CoordinatorEntity:
        """Minimal coordinator entity stub."""

        def __init__(self, coordinator):
            self.coordinator = coordinator

    ha_update_coordinator.CoordinatorEntity = CoordinatorEntity
    sys.modules["homeassistant.helpers.update_coordinator"] = ha_update_coordinator

    ha_const = types.ModuleType("homeassistant.const")

    class UnitOfTemperature:
        CELSIUS = "degC"
        FAHRENHEIT = "degF"

    class UnitOfPressure:
        HPA = "hPa"
        KPA = "kPa"
        MBAR = "mbar"
        INHG = "inHg"

    class UnitOfPrecipitationDepth:
        MILLIMETERS = "mm"
        INCHES = "in"

    class UnitOfVolumetricFlux:
        MILLIMETERS_PER_HOUR = "mm/h"
        INCHES_PER_HOUR = "in/h"

    class UnitOfSpeed:
        METERS_PER_SECOND = "m/s"
        MILES_PER_HOUR = "mph"
        KILOMETERS_PER_HOUR = "km/h"
        KNOTS = "kts"

    ha_const.UnitOfTemperature = UnitOfTemperature
    ha_const.UnitOfPressure = UnitOfPressure
    ha_const.UnitOfPrecipitationDepth = UnitOfPrecipitationDepth
    ha_const.UnitOfVolumetricFlux = UnitOfVolumetricFlux
    ha_const.UnitOfSpeed = UnitOfSpeed
    sys.modules["homeassistant.const"] = ha_const

    integration_const = types.ModuleType("custom_components.cumulusmx.const")
    integration_const.DOMAIN = "cumulusmx"
    integration_const.SENSOR_TYPES = {
        "temp": {
            "device": "weather",
            "name": "Temperature",
            "device_class": SensorDeviceClass.TEMPERATURE,
            "state_class": "measurement",
            "entity_category": None,
            "options": None,
            "suggested_display_precision": None,
            "unit": UnitOfTemperature.CELSIUS,
            "icon": None,
            "translation_key": "temp",
        },
        "press": {
            "device": "weather",
            "name": "Pressure",
            "device_class": SensorDeviceClass.PRESSURE,
            "state_class": "measurement",
            "entity_category": None,
            "options": None,
            "suggested_display_precision": 1,
            "unit": UnitOfPressure.HPA,
            "icon": None,
            "translation_key": "press",
        },
        "rfall": {
            "device": "weather",
            "name": "Rainfall",
            "device_class": SensorDeviceClass.PRECIPITATION,
            "state_class": "total",
            "entity_category": None,
            "options": None,
            "suggested_display_precision": None,
            "unit": UnitOfPrecipitationDepth.MILLIMETERS,
            "icon": None,
            "translation_key": "rfall",
        },
        "rrate": {
            "device": "weather",
            "name": "Rainfall Rate",
            "device_class": SensorDeviceClass.PRECIPITATION_INTENSITY,
            "state_class": "measurement",
            "entity_category": None,
            "options": None,
            "suggested_display_precision": None,
            "unit": UnitOfVolumetricFlux.MILLIMETERS_PER_HOUR,
            "icon": None,
            "translation_key": "rrate",
        },
        "wspeed": {
            "device": "weather",
            "name": "Wind Speed",
            "device_class": SensorDeviceClass.WIND_SPEED,
            "state_class": "measurement",
            "entity_category": None,
            "options": None,
            "suggested_display_precision": 1,
            "unit": UnitOfSpeed.KILOMETERS_PER_HOUR,
            "icon": None,
            "translation_key": "wspeed",
        },
        "wdir": {
            "device": "weather",
            "name": "Wind Direction",
            "device_class": SensorDeviceClass.ENUM,
            "state_class": None,
            "entity_category": None,
            "options": [
                "n",
                "nne",
                "ne",
                "ene",
                "e",
                "ese",
                "se",
                "sse",
                "s",
                "ssw",
                "sw",
                "wsw",
                "w",
                "wnw",
                "nw",
                "nnw",
            ],
            "suggested_display_precision": None,
            "unit": None,
            "icon": "mdi:compass",
            "translation_key": "wdir",
        },
    }
    sys.modules["custom_components.cumulusmx.const"] = integration_const

    coordinator_module = types.ModuleType("custom_components.cumulusmx.coordinator")

    class CumulusMXCoordinator:
        """Minimal coordinator type stub."""

    coordinator_module.CumulusMXCoordinator = CumulusMXCoordinator
    sys.modules["custom_components.cumulusmx.coordinator"] = coordinator_module

    spec = importlib.util.spec_from_file_location(
        "custom_components.cumulusmx.sensor", sensor_path
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


SENSOR_MODULE = _load_sensor_module()


class SensorHelpersTestCase(unittest.TestCase):
    """Tests for helper functions in sensor.py."""

    def test_get_station_manufacturer_known_and_fallback_values(self):
        self.assertEqual(
            SENSOR_MODULE.get_station_manufacturer("Davis Vantage Pro2"), "Davis"
        )
        self.assertEqual(
            SENSOR_MODULE.get_station_manufacturer("La Crosse WS2350"), "La Crosse"
        )
        self.assertEqual(
            SENSOR_MODULE.get_station_manufacturer("Mystery Station 2000"), "Mystery"
        )
        self.assertEqual(SENSOR_MODULE.get_station_manufacturer(None), "Unknown")

    def test_get_device_info_for_airlink_and_weather_station(self):
        airlink_info = SENSOR_MODULE.get_device_info(
            "airlink", "weather.local", 8998, "entry-1"
        )
        self.assertEqual(airlink_info.manufacturer, "Davis")
        self.assertEqual(airlink_info.model, "AirLink")
        self.assertEqual(airlink_info.translation_key, "airlink")
        self.assertEqual(airlink_info.via_device, ("cumulusmx", "entry-1"))

        weather_info = SENSOR_MODULE.get_device_info(
            "weather", "weather.local", 8998, "entry-1", "Ecowitt GW2000"
        )
        self.assertEqual(weather_info.manufacturer, "Ecowitt")
        self.assertEqual(weather_info.model, "Ecowitt GW2000")
        self.assertEqual(weather_info.translation_key, "weather_station")
        self.assertEqual(
            weather_info.translation_placeholders,
            {"station_type": "Ecowitt GW2000"},
        )

    def test_get_device_type_returns_none_for_unknown_keys(self):
        self.assertEqual(SENSOR_MODULE.get_device_type("temp"), "weather")
        self.assertIsNone(SENSOR_MODULE.get_device_type("unknown_key"))


class CumulusMXSensorTestCase(unittest.TestCase):
    """Tests for the CumulusMXSensor entity."""

    def _make_coordinator(self, data):
        return SimpleNamespace(
            data=data,
            host="weather.local",
            port=8998,
            config_entry=SimpleNamespace(entry_id="entry-1"),
        )

    def _make_sensor(self, key, sensor_info=None, data=None, device_type="weather"):
        if sensor_info is None:
            sensor_info = SENSOR_MODULE.SENSOR_TYPES[key].copy()
        if data is None:
            data = {key: "1"}
        coordinator = self._make_coordinator(data)
        return SENSOR_MODULE.CumulusMXSensor(
            coordinator, key, sensor_info.copy(), device_type
        )

    def test_native_value_normalizes_numeric_strings(self):
        comma_sensor = self._make_sensor("temp", data={"temp": "12,3"})
        dot_sensor = self._make_sensor("temp", data={"temp": "12.3"})
        text_sensor = self._make_sensor("temp", data={"temp": "offline"})

        self.assertEqual(comma_sensor.native_value, 12.3)
        self.assertEqual(dot_sensor.native_value, 12.3)
        self.assertEqual(text_sensor.native_value, "offline")

    def test_native_value_normalizes_enum_values_and_rejects_invalid_values(self):
        enum_info = SENSOR_MODULE.SENSOR_TYPES["wdir"].copy()

        valid_sensor = self._make_sensor("wdir", sensor_info=enum_info, data={"wdir": " NNW "})
        invalid_sensor = self._make_sensor(
            "wdir", sensor_info=enum_info, data={"wdir": "North"}
        )
        blank_sensor = self._make_sensor("wdir", sensor_info=enum_info, data={"wdir": "-"})

        self.assertEqual(valid_sensor.native_value, "nnw")
        self.assertIsNone(invalid_sensor.native_value)
        self.assertIsNone(blank_sensor.native_value)

    def test_unique_id_native_unit_icon_and_device_info(self):
        sensor = self._make_sensor(
            "temp",
            data={"temp": "20.5", "tempunit": "&#176;C", "stationtype": "Ecowitt GW2000"},
        )

        self.assertEqual(sensor.unique_id, "cumulusmx_entry-1_weather_temp")
        self.assertNotEqual(sensor.native_unit_of_measurement, "&#176;C")
        self.assertTrue(sensor.native_unit_of_measurement.endswith("C"))
        self.assertEqual(sensor.device_class, SENSOR_MODULE.SensorDeviceClass.TEMPERATURE)
        self.assertEqual(sensor.device_info.manufacturer, "Ecowitt")
        self.assertEqual(sensor.device_info.model, "Ecowitt GW2000")
        self.assertIsNone(sensor.icon)

    def test_static_unit_is_used_when_no_dynamic_unit_exists(self):
        sensor = self._make_sensor("press", data={"press": "1013.2"})
        self.assertEqual(
            sensor.native_unit_of_measurement, SENSOR_MODULE.UnitOfPressure.HPA
        )


class AsyncSetupEntryTestCase(unittest.IsolatedAsyncioTestCase):
    """Tests for async_setup_entry."""

    async def test_async_setup_entry_adds_supported_sensors_and_sets_units(self):
        coordinator = SimpleNamespace(
            data={
                "tempunit": "&#176;F",
                "pressunit": "in",
                "rainunit": "inches",
                "windunit": "mph",
                "temp": "72.0",
                "press": "29.92",
                "rfall": "0.42",
                "rrate": "0.10",
                "wspeed": "8.0",
                "wdir": "SW",
                "unknown": "ignored",
            },
            host="weather.local",
            port=8998,
            config_entry=SimpleNamespace(entry_id="entry-1"),
        )

        async def async_refresh():
            return None

        coordinator.async_refresh = async_refresh

        hass = SimpleNamespace()
        config_entry = SimpleNamespace(entry_id="entry-1", runtime_data=coordinator)
        added_entities = []

        def async_add_entities(entities):
            added_entities.extend(entities)

        await SENSOR_MODULE.async_setup_entry(hass, config_entry, async_add_entities)

        self.assertEqual([entity._key for entity in added_entities], ["temp", "press", "rfall", "rrate", "wspeed", "wdir"])

        entities_by_key = {entity._key: entity for entity in added_entities}
        self.assertEqual(
            entities_by_key["press"]._sensor_info["unit"], SENSOR_MODULE.UnitOfPressure.INHG
        )
        self.assertEqual(
            entities_by_key["rfall"]._sensor_info["unit"],
            SENSOR_MODULE.UnitOfPrecipitationDepth.INCHES,
        )
        self.assertEqual(
            entities_by_key["rrate"]._sensor_info["unit"],
            SENSOR_MODULE.UnitOfVolumetricFlux.INCHES_PER_HOUR,
        )
        self.assertEqual(
            entities_by_key["wspeed"]._sensor_info["unit"],
            SENSOR_MODULE.UnitOfSpeed.MILES_PER_HOUR,
        )


if __name__ == "__main__":
    unittest.main()
