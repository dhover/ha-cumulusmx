"""Support for CumulusMX software update entity."""

import aiohttp

from homeassistant.components.update import UpdateEntity
from homeassistant.helpers.entity import DeviceInfo
from .const import DOMAIN,GITHUB_API_URL


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the update entity based on a config entry."""
    coordinator = hass.data["cumulusmx"][config_entry.entry_id]
    async_add_entities([CumulusMXUpdateEntity(coordinator)], True)

class CumulusMXUpdateEntity(UpdateEntity):
    """CumulusMX software update entity."""
    _attr_has_entity_name = True

    def __init__(self, coordinator):
        self.coordinator = coordinator
        self._attr_latest_version = None
        self._attr_installed_version = None
        self._attr_title = "CumulusMX Software"

    async def async_update(self):
        """Fetch the latest version information from GitHub."""
        await self.coordinator.async_refresh()
        self._attr_installed_version = f"b{self.coordinator.data.get('build')}"

        # Fetch latest version from GitHub
        async with aiohttp.ClientSession() as session:
            async with session.get(GITHUB_API_URL) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    self._attr_latest_version = data.get("tag_name")
                else:
                    self._attr_latest_version = None

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
        return "cumulusmx_software_update"

    @property
    def name(self):
        """Return the name of the update entity."""
        return "Update"

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        if not self.coordinator.data:
            return None

        version = self.coordinator.data.get('version') or ""
        build = self.coordinator.data.get('build') or ""
        return DeviceInfo(
            identifiers={(DOMAIN, self.coordinator.config_entry.entry_id)},
            name="CumulusMX Software",
            manufacturer="CumulusMX",
            model="Software",
            #hw_version=hardware.get("revision", ""),
            #serial_number=serial_number,
            sw_version=f"{version} build {build}",
        )
