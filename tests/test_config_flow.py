"""Unit tests for custom_components.cumulusmx.config_flow."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import types
import unittest
from types import SimpleNamespace


def _load_config_flow_module():
    """Load the config flow module with lightweight Home Assistant stubs."""
    config_flow_path = (
        Path(__file__).resolve().parents[1]
        / "custom_components"
        / "cumulusmx"
        / "config_flow.py"
    )

    for module_name in (
        "custom_components.cumulusmx.config_flow",
        "custom_components.cumulusmx.cumulusmx",
        "custom_components.cumulusmx.const",
        "custom_components.cumulusmx",
        "custom_components",
        "homeassistant",
        "homeassistant.config_entries",
        "homeassistant.core",
        "homeassistant.helpers",
        "homeassistant.helpers.selector",
        "voluptuous",
    ):
        sys.modules.pop(module_name, None)

    voluptuous = types.ModuleType("voluptuous")

    class Schema:
        """Minimal voluptuous Schema stub."""

        def __init__(self, schema):
            self.schema = schema

    class Required:
        """Minimal voluptuous Required marker stub."""

        def __init__(self, key, default=None):
            self.key = key
            self.default = default

        def __hash__(self):
            return hash((self.key, self.default))

        def __eq__(self, other):
            return (
                isinstance(other, Required)
                and self.key == other.key
                and self.default == other.default
            )

    voluptuous.Schema = Schema
    voluptuous.Required = Required
    sys.modules["voluptuous"] = voluptuous

    custom_components = types.ModuleType("custom_components")
    custom_components.__path__ = [str(config_flow_path.parents[1])]
    sys.modules["custom_components"] = custom_components

    cumulusmx_pkg = types.ModuleType("custom_components.cumulusmx")
    cumulusmx_pkg.__path__ = [str(config_flow_path.parent)]
    sys.modules["custom_components.cumulusmx"] = cumulusmx_pkg

    homeassistant = types.ModuleType("homeassistant")
    sys.modules["homeassistant"] = homeassistant

    ha_config_entries = types.ModuleType("homeassistant.config_entries")

    class ConfigEntry:
        """Minimal config entry stub."""

        def __init__(
            self,
            *,
            entry_id="entry-1",
            data=None,
            options=None,
            unique_id=None,
        ):
            self.entry_id = entry_id
            self.data = data or {}
            self.options = options or {}
            self.unique_id = unique_id
            self.title = None

    class ConfigFlow:
        """Minimal config flow stub."""

        def __init_subclass__(cls, **kwargs):
            return super().__init_subclass__()

        async def async_set_unique_id(self, unique_id):
            self._unique_id = unique_id

        def async_show_form(self, **kwargs):
            return {"type": "form", **kwargs}

        def async_create_entry(self, **kwargs):
            return {"type": "create_entry", **kwargs}

        def async_abort(self, **kwargs):
            return {"type": "abort", **kwargs}

        def add_suggested_values_to_schema(self, data_schema, suggested_values):
            return (data_schema, suggested_values)

        def async_update_entry(self, entry, **kwargs):
            self.updated_entry = (entry, kwargs)
            entry.data = kwargs.get("data", entry.data)
            entry.options = kwargs.get("options", entry.options)
            entry.unique_id = kwargs.get("unique_id", entry.unique_id)
            entry.title = kwargs.get("title", entry.title)

        async def async_reload(self, entry_id):
            await self.hass.config_entries.async_reload(entry_id)

        async def async_update_reload_and_abort(
            self,
            entry,
            data_updates=None,
            options_updates=None,
            unique_id=None,
        ):
            self.async_update_entry(
                entry,
                data=data_updates or entry.data,
                options=options_updates or entry.options,
                unique_id=unique_id or entry.unique_id,
            )
            await self.async_reload(entry.entry_id)
            return self.async_abort(reason="reconfigure_successful")

        def _get_reconfigure_entry(self):
            return self._reconfigure_entry

    class OptionsFlow:
        """Minimal options flow stub."""

        def async_show_form(self, **kwargs):
            return {"type": "form", **kwargs}

        def async_create_entry(self, **kwargs):
            return {"type": "create_entry", **kwargs}

        def add_suggested_values_to_schema(self, data_schema, suggested_values):
            return (data_schema, suggested_values)

    ha_config_entries.ConfigEntry = ConfigEntry
    ha_config_entries.ConfigFlow = ConfigFlow
    ha_config_entries.OptionsFlow = OptionsFlow
    homeassistant.config_entries = ha_config_entries
    sys.modules["homeassistant.config_entries"] = ha_config_entries

    ha_core = types.ModuleType("homeassistant.core")
    ha_core.callback = lambda func: func
    sys.modules["homeassistant.core"] = ha_core

    ha_helpers = types.ModuleType("homeassistant.helpers")
    sys.modules["homeassistant.helpers"] = ha_helpers

    ha_selector = types.ModuleType("homeassistant.helpers.selector")

    class SelectSelectorMode:
        LIST = "list"

    class SelectSelectorConfig:
        def __init__(self, **kwargs):
            self.kwargs = kwargs

    class SelectSelector:
        def __init__(self, config):
            self.config = config

    ha_selector.SelectSelectorMode = SelectSelectorMode
    ha_selector.SelectSelectorConfig = SelectSelectorConfig
    ha_selector.SelectSelector = SelectSelector
    sys.modules["homeassistant.helpers.selector"] = ha_selector

    integration_const = types.ModuleType("custom_components.cumulusmx.const")
    integration_const.DOMAIN = "cumulusmx"
    integration_const.CONF_HOST = "host"
    integration_const.CONF_PORT = "port"
    integration_const.CONF_WEBTAGS = "webtags"
    integration_const.DEFAULT_HOST = "192.168.x.x"
    integration_const.DEFAULT_PORT = 8998
    integration_const.DEFAULT_WEBTAGS = ["temp", "hum"]
    integration_const.ALL_WEBTAG_OPTIONS = ["temp", "hum", "press"]

    def normalize_configurable_webtags(webtags):
        return [tag for tag in webtags if tag not in {"version", "build"}]

    integration_const.normalize_configurable_webtags = normalize_configurable_webtags
    sys.modules["custom_components.cumulusmx.const"] = integration_const

    api_module = types.ModuleType("custom_components.cumulusmx.cumulusmx")

    async def _async_validate_connection(hass, user_input):
        return True

    api_module._async_validate_connection = _async_validate_connection
    sys.modules["custom_components.cumulusmx.cumulusmx"] = api_module

    spec = importlib.util.spec_from_file_location(
        "custom_components.cumulusmx.config_flow", config_flow_path
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


CONFIG_FLOW_MODULE = _load_config_flow_module()


class ConfigEntriesManager:
    """Minimal config entries manager stub."""

    def __init__(self, entries=None):
        self._entries = entries or []
        self.updated_entry = None
        self.reloaded_entry_id = None

    def async_entries(self, domain):
        return self._entries

    def async_update_entry(self, entry, **kwargs):
        self.updated_entry = (entry, kwargs)
        entry.data = kwargs.get("data", entry.data)
        entry.options = kwargs.get("options", entry.options)
        entry.unique_id = kwargs.get("unique_id", entry.unique_id)
        entry.title = kwargs.get("title", entry.title)

    async def async_reload(self, entry_id):
        self.reloaded_entry_id = entry_id


class ConfigFlowTestCase(unittest.IsolatedAsyncioTestCase):
    """Tests for the CumulusMX config flow."""

    def _make_flow(self, entries=None):
        flow = CONFIG_FLOW_MODULE.CumulusMXConfigFlow()
        flow.hass = SimpleNamespace(config_entries=ConfigEntriesManager(entries))
        return flow

    def _make_entry(self, **kwargs):
        return CONFIG_FLOW_MODULE.config_entries.ConfigEntry(**kwargs)

    def _set_validator(self, result):
        calls = []

        async def validate(hass, user_input):
            calls.append(user_input)
            return result

        CONFIG_FLOW_MODULE._async_validate_connection = validate
        return calls

    async def test_user_step_creates_entry_with_unique_id(self):
        calls = self._set_validator(True)
        flow = self._make_flow()

        result = await flow.async_step_user({"host": "Weather.Local", "port": 8998})

        self.assertEqual(result["type"], "create_entry")
        self.assertEqual(result["title"], "Weather.Local:8998")
        self.assertEqual(result["data"]["webtags"], ["temp", "hum"])
        self.assertEqual(flow._unique_id, "weather.local:8998")
        self.assertEqual(len(calls), 1)

    async def test_user_step_aborts_existing_entry_with_same_host_and_port(self):
        calls = self._set_validator(True)
        existing_entry = self._make_entry(data={"host": "weather.local", "port": 8998})
        flow = self._make_flow([existing_entry])

        result = await flow.async_step_user({"host": "WEATHER.LOCAL", "port": 8998})

        self.assertEqual(result, {"type": "abort", "reason": "already_configured"})
        self.assertEqual(calls, [])

    async def test_user_step_shows_error_when_connection_fails(self):
        self._set_validator(False)
        flow = self._make_flow()

        result = await flow.async_step_user({"host": "weather.local", "port": 8998})

        self.assertEqual(result["type"], "form")
        self.assertEqual(result["step_id"], "user")
        self.assertEqual(result["errors"], {"base": "cannot_connect"})

    async def test_reconfigure_updates_entry_unique_id_and_reloads(self):
        self._set_validator(True)
        entry = self._make_entry(
            entry_id="entry-1",
            data={"host": "old.local", "port": 8998, "webtags": ["temp"]},
        )
        flow = self._make_flow([entry])
        flow._reconfigure_entry = entry

        result = await flow.async_step_reconfigure(
            {"host": "weather.local", "port": 8999}
        )

        self.assertEqual(result, {"type": "abort", "reason": "reconfigure_successful"})
        self.assertEqual(entry.data["host"], "weather.local")
        self.assertEqual(entry.data["port"], 8999)
        self.assertEqual(entry.unique_id, "weather.local:8999")
        self.assertEqual(flow.hass.config_entries.reloaded_entry_id, "entry-1")

    async def test_reconfigure_aborts_when_target_entry_already_exists(self):
        self._set_validator(True)
        entry = self._make_entry(
            entry_id="entry-1",
            data={"host": "old.local", "port": 8998},
        )
        existing_entry = self._make_entry(
            entry_id="entry-2",
            data={"host": "weather.local", "port": 8999},
        )
        flow = self._make_flow([entry, existing_entry])
        flow._reconfigure_entry = entry

        result = await flow.async_step_reconfigure(
            {"host": "weather.local", "port": 8999}
        )

        self.assertEqual(result, {"type": "abort", "reason": "already_configured"})

    async def test_options_flow_normalizes_webtags(self):
        config_entry = self._make_entry(
            data={"host": "weather.local", "port": 8998, "webtags": ["temp"]},
            options={"webtags": ["temp", "version"]},
        )
        options_flow = CONFIG_FLOW_MODULE.CumulusMXOptionsFlowHandler()
        options_flow.config_entry = config_entry

        result = await options_flow.async_step_init({"webtags": ["press", "version"]})

        self.assertEqual(result, {"type": "create_entry", "data": {"webtags": ["press"]}})

    async def test_options_flow_uses_default_when_no_webtags_remain(self):
        config_entry = self._make_entry(
            data={"host": "weather.local", "port": 8998},
            options={},
        )
        options_flow = CONFIG_FLOW_MODULE.CumulusMXOptionsFlowHandler()
        options_flow.config_entry = config_entry

        result = await options_flow.async_step_init({"webtags": ["version"]})

        self.assertEqual(
            result,
            {"type": "create_entry", "data": {"webtags": ["temp", "hum"]}},
        )


if __name__ == "__main__":
    unittest.main()
