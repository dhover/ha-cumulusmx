"""Unit tests for custom_components.cumulusmx.update."""

from __future__ import annotations

from dataclasses import dataclass
import importlib.util
from pathlib import Path
import sys
import types
import unittest
from types import SimpleNamespace


def _load_update_module():
    """Load the update module with lightweight Home Assistant stubs."""
    update_path = (
        Path(__file__).resolve().parents[1]
        / "custom_components"
        / "cumulusmx"
        / "update.py"
    )

    for module_name in (
        "custom_components.cumulusmx.update",
        "custom_components.cumulusmx.const",
        "custom_components.cumulusmx",
        "custom_components",
        "homeassistant",
        "homeassistant.components",
        "homeassistant.components.update",
        "homeassistant.helpers",
        "homeassistant.helpers.aiohttp_client",
        "homeassistant.helpers.entity",
    ):
        sys.modules.pop(module_name, None)

    custom_components = types.ModuleType("custom_components")
    custom_components.__path__ = [str(update_path.parents[1])]
    sys.modules["custom_components"] = custom_components

    cumulusmx_pkg = types.ModuleType("custom_components.cumulusmx")
    cumulusmx_pkg.__path__ = [str(update_path.parent)]
    sys.modules["custom_components.cumulusmx"] = cumulusmx_pkg

    homeassistant = types.ModuleType("homeassistant")
    sys.modules["homeassistant"] = homeassistant

    ha_components = types.ModuleType("homeassistant.components")
    sys.modules["homeassistant.components"] = ha_components

    ha_update = types.ModuleType("homeassistant.components.update")

    class UpdateDeviceClass:
        FIRMWARE = "firmware"

    class UpdateEntity:
        """Minimal update entity stub."""

    ha_update.UpdateDeviceClass = UpdateDeviceClass
    ha_update.UpdateEntity = UpdateEntity
    sys.modules["homeassistant.components.update"] = ha_update

    ha_helpers = types.ModuleType("homeassistant.helpers")
    sys.modules["homeassistant.helpers"] = ha_helpers

    aiohttp_mod = types.ModuleType("aiohttp")
    class ClientError(Exception):
        pass
    aiohttp_mod.ClientError = ClientError
    sys.modules["aiohttp"] = aiohttp_mod

    ha_helpers_event = types.ModuleType("homeassistant.helpers.event")
    ha_helpers_event.async_track_time_interval = lambda hass, action, interval: lambda: None
    sys.modules["homeassistant.helpers.event"] = ha_helpers_event

    ha_aiohttp = types.ModuleType("homeassistant.helpers.aiohttp_client")
    ha_aiohttp.async_get_clientsession = lambda hass: hass.session
    sys.modules["homeassistant.helpers.aiohttp_client"] = ha_aiohttp

    ha_entity = types.ModuleType("homeassistant.helpers.entity")

    @dataclass(eq=True)
    class DeviceInfo:
        identifiers: set | None = None
        translation_key: str | None = None
        manufacturer: str | None = None
        model: str | None = None
        configuration_url: str | None = None
        sw_version: str | None = None

    ha_entity.DeviceInfo = DeviceInfo
    sys.modules["homeassistant.helpers.entity"] = ha_entity

    integration_const = types.ModuleType("custom_components.cumulusmx.const")
    integration_const.DOMAIN = "cumulusmx"
    integration_const.GITHUB_API_URL = "https://api.github.com/example/releases/latest"
    sys.modules["custom_components.cumulusmx.const"] = integration_const

    spec = importlib.util.spec_from_file_location(
        "custom_components.cumulusmx.update", update_path
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


UPDATE_MODULE = _load_update_module()


class ResponseStub:
    """Minimal aiohttp response context manager stub."""

    def __init__(self, *, status=200, data=None, json_error=None):
        self.status = status
        self._data = data or {}
        self._json_error = json_error

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, traceback):
        return False

    async def json(self):
        if self._json_error:
            raise self._json_error
        return self._data


class SessionStub:
    """Minimal aiohttp client session stub."""

    def __init__(self, response=None, error=None):
        self.response = response
        self.error = error
        self.timeout = None
        self.url = None

    def get(self, url, *, timeout=None):
        self.url = url
        self.timeout = timeout
        if self.error:
            raise self.error
        return self.response


class UpdateEntityTestCase(unittest.IsolatedAsyncioTestCase):
    """Tests for the CumulusMX update entity."""

    def _make_entity(self, *, session, version="CumulusMX v4.5.6"):
        async def async_refresh():
            return None

        coordinator = SimpleNamespace(
            async_refresh=async_refresh,
            data={"version": version, "build": "1234"},
            host="weather.local",
            port=8998,
            config_entry=SimpleNamespace(entry_id="entry-1"),
        )
        entity = UPDATE_MODULE.CumulusMXUpdateEntity(coordinator)
        entity.hass = SimpleNamespace(session=session)
        return entity

    def test_extract_semver_and_version_comparison(self):
        self.assertEqual(UPDATE_MODULE.extract_semver("CumulusMX v4.5.6"), "4.5.6")
        self.assertIsNone(UPDATE_MODULE.extract_semver("latest"))
        self.assertTrue(UPDATE_MODULE.CumulusMXUpdateEntity(None).version_is_newer("4.5.7", "4.5.6"))
        self.assertFalse(UPDATE_MODULE.CumulusMXUpdateEntity(None).version_is_newer("latest", "4.5.6"))

    async def test_async_update_fetches_latest_release_with_timeout(self):
        session = SessionStub(
            ResponseStub(
                data={
                    "name": "CumulusMX 5.0.0",
                    "tag_name": "v5.0.0",
                    "html_url": "https://example.test/release",
                }
            )
        )
        entity = self._make_entity(session=session)

        await entity.async_update()

        self.assertEqual(entity.installed_version, "4.5.6")
        self.assertEqual(entity.latest_version, "5.0.0")
        self.assertEqual(entity._attr_release_url, "https://example.test/release")
        self.assertEqual(session.timeout, UPDATE_MODULE.UPDATE_CHECK_TIMEOUT)

    async def test_async_update_handles_github_errors_without_raising(self):
        session = SessionStub(error=TimeoutError("timed out"))
        entity = self._make_entity(session=session)

        await entity.async_update()

        self.assertEqual(entity.installed_version, "4.5.6")
        self.assertIsNone(entity.latest_version)
        self.assertIsNone(entity._attr_release_url)

    async def test_async_update_handles_non_successful_status(self):
        session = SessionStub(ResponseStub(status=503))
        entity = self._make_entity(session=session)

        await entity.async_update()

        self.assertEqual(entity.installed_version, "4.5.6")
        self.assertIsNone(entity.latest_version)
        self.assertIsNone(entity._attr_release_url)


if __name__ == "__main__":
    unittest.main()
