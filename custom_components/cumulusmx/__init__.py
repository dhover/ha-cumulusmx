""" CumulusMX integration for Home Assistant."""

from homeassistant.helpers import config_validation as cv
from homeassistant.helpers import device_registry as dr
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.const import Platform

from .const import DOMAIN
from .coordinator import CumulusMXCoordinator
# from . import config_flow  # Zorgt dat de options flow wordt geregistreerd

PLATFORMS = [Platform.SENSOR, Platform.UPDATE]

CONFIG_SCHEMA = cv.config_entry_only_config_schema("cumulusmx")

type CumulusMXConfigEntry = ConfigEntry[CumulusMXCoordinator]


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the CumulusMX integration from configuration.yaml (not used)."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: CumulusMXConfigEntry):
    """Set up CumulusMX from a config entry."""
    coordinator = CumulusMXCoordinator(hass, entry)
    await coordinator.async_config_entry_first_refresh()
    entry.runtime_data = coordinator

    device_registry = dr.async_get(hass)
    device_registry.async_get_or_create(
        config_entry_id=entry.entry_id,
        identifiers={(DOMAIN, entry.entry_id)},
        name="CumulusMX",
        manufacturer="CumulusMX",
        model="CumulusMX",
        configuration_url=f"http://{coordinator.host}:{coordinator.port}",
    )

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    entry.async_on_unload(entry.add_update_listener(async_update_options))
    return True


async def async_unload_entry(hass: HomeAssistant, entry: CumulusMXConfigEntry):
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)


async def async_update_options(hass: HomeAssistant, entry: CumulusMXConfigEntry):
    """Handle options update."""
    await hass.config_entries.async_reload(entry.entry_id)
