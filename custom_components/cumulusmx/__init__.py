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


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the CumulusMX integration from configuration.yaml (not used)."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up CumulusMX from a config entry."""
    coordinator = CumulusMXCoordinator(hass, entry)
    await coordinator.async_config_entry_first_refresh()

    device_registry = dr.async_get(hass)
    device_registry.async_get_or_create(
        config_entry_id=entry.entry_id,
        identifiers={(DOMAIN, entry.entry_id)},
        name="CumulusMX",
        manufacturer="CumulusMX",
        model="CumulusMX",
        configuration_url=f"http://{coordinator.host}:{coordinator.port}",
    )

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    entry.async_on_unload(entry.add_update_listener(async_update_options))
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    hass.data[DOMAIN].pop(entry.entry_id)
    return True


async def async_update_options(hass: HomeAssistant, entry: ConfigEntry):
    """Handle options update."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    await coordinator.async_reload_config()
    await coordinator.async_request_refresh()
