"""Support for CumulusMX software update entity."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

from homeassistant.components.update import UpdateDeviceClass, UpdateEntity
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from .const import DOMAIN, GITHUB_API_URL

if TYPE_CHECKING:
    from . import CumulusMXConfigEntry

SEMVER_PATTERN = re.compile(r"(\d+)\.(\d+)\.(\d+)")


def extract_semver(value: str | None) -> str | None:
    """Extract a semantic version in x.y.z format from a string."""
    if not value:
        return None

    match = SEMVER_PATTERN.search(value)
    if not match:
        return None

    return ".".join(match.groups())


def semver_to_tuple(version: str | None) -> tuple[int, int, int] | None:
    """Convert an x.y.z version string to a tuple for comparisons."""
    parsed = extract_semver(version)
    if not parsed:
        return None

    major, minor, patch = parsed.split(".")
    return int(major), int(minor), int(patch)


async def async_setup_entry(hass, config_entry: CumulusMXConfigEntry, async_add_entities):
    """Set up the update entity based on a config entry."""
    coordinator = config_entry.runtime_data
    async_add_entities([CumulusMXUpdateEntity(coordinator)], True)


class CumulusMXUpdateEntity(UpdateEntity):
    """CumulusMX Hub update entity."""

    _attr_has_entity_name = True
    _attr_translation_key = "hub_update"
    _attr_device_class = UpdateDeviceClass.FIRMWARE

    def __init__(self, coordinator):
        self.coordinator = coordinator
        self._attr_latest_version = None
        self._attr_installed_version = None
        self._attr_release_url = None
        self._attr_title = "CumulusMX Hub"

    async def async_update(self):
        """Fetch the latest version information from GitHub."""
        await self.coordinator.async_refresh()
        self._attr_installed_version = extract_semver(
            self.coordinator.data.get("version")
        )

        # Fetch latest version from GitHub
        session = async_get_clientsession(self.hass)
        async with session.get(GITHUB_API_URL) as resp:
            if resp.status == 200:
                data = await resp.json()
                self._attr_latest_version = (
                    extract_semver(data.get("name"))
                    or extract_semver(data.get("tag_name"))
                )
                self._attr_release_url = data.get("html_url")
            else:
                self._attr_latest_version = None
                self._attr_release_url = None

    @property
    def installed_version(self):
        """Return the installed version."""
        return self._attr_installed_version

    @property
    def latest_version(self):
        """Return the latest version."""
        return self._attr_latest_version

    @property
    def unique_id(self):
        """Return a unique ID for the update entity."""
        return f"cumulusmx_{self.coordinator.config_entry.entry_id}_hub_update"

    def version_is_newer(self, latest_version: str, installed_version: str) -> bool:
        """Return True if the latest version is newer than the installed version."""
        latest = semver_to_tuple(latest_version)
        installed = semver_to_tuple(installed_version)
        if latest is None or installed is None:
            return False
        return latest > installed

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        if not self.coordinator.data:
            return None

        version = self._attr_installed_version or ""
        build = self.coordinator.data.get("build") or ""
        return DeviceInfo(
            identifiers={(DOMAIN, self.coordinator.config_entry.entry_id)},
            translation_key="hub",
            manufacturer="CumulusMX",
            model="Hub",
            configuration_url=f"http://{self.coordinator.host}:{self.coordinator.port}",
            sw_version=f"{version} build {build}",
        )
