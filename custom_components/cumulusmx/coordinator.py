"""CumulusMX integration coordinator to manage data updates."""

from datetime import timedelta
import logging

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from aiohttp import ClientError
from .const import create_sensor_post_body, normalize_webtags

from .const import (
    DOMAIN,
    CONF_HOST,
    CONF_PORT,
    CONF_WEBTAGS,
    CONF_UPDATE_INTERVAL,
    DEFAULT_UPDATE_INTERVAL,
    SENSOR_API_URL,
)

from .cumulusmx import CumulusMXApi  # <-- Import the API class

_LOGGER = logging.getLogger(__name__)


class CumulusMXCoordinator(DataUpdateCoordinator):
    """CumulusMX data update coordinator."""

    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry):
        self.hass = hass
        self.host = config_entry.options.get(CONF_HOST, config_entry.data.get(CONF_HOST))
        self.port = config_entry.options.get(CONF_PORT, config_entry.data.get(CONF_PORT))
        self.url = SENSOR_API_URL.format(host=self.host, port=self.port)
        webtags = normalize_webtags(
            config_entry.options.get(CONF_WEBTAGS, config_entry.data.get(CONF_WEBTAGS))
        )
        webtags.extend(["tempunit", "pressunit", "rainunit", "windunit"])
        self.post_body = create_sensor_post_body(webtags)
        _LOGGER.debug("Send to CumulusMX: %s", self.post_body)
        update_interval = timedelta(seconds=config_entry.options.get(CONF_UPDATE_INTERVAL,
            config_entry.data.get(CONF_UPDATE_INTERVAL, DEFAULT_UPDATE_INTERVAL)))

        self.api = CumulusMXApi(self.hass, self.url, self.post_body)

        super().__init__(
            hass,
            _LOGGER,
            config_entry=config_entry,
            name=f"{DOMAIN} Coordinator",
            update_interval=update_interval,
        )

    async def async_reload_config(self):
        """Reload configuration from config entry."""
        self.host = self.config_entry.options.get(CONF_HOST, self.config_entry.data.get(CONF_HOST))
        self.port = self.config_entry.options.get(CONF_PORT, self.config_entry.data.get(CONF_PORT))
        self.url = SENSOR_API_URL.format(host=self.host, port=self.port)
        webtags = normalize_webtags(
            self.config_entry.options.get(CONF_WEBTAGS, self.config_entry.data.get(CONF_WEBTAGS))
        )
        webtags.extend(["tempunit", "pressunit", "rainunit", "windunit"])
        self.post_body = create_sensor_post_body(webtags)
        _LOGGER.debug("Send to CumulusMX: %s", self.post_body)
        update_interval = timedelta(seconds=self.config_entry.options.get(CONF_UPDATE_INTERVAL,
            self.config_entry.data.get(CONF_UPDATE_INTERVAL, DEFAULT_UPDATE_INTERVAL)))
        self.update_interval = update_interval
        self.api = CumulusMXApi(self.hass, self.url, self.post_body)

    async def _async_update_data(self):
        try:
            data = await self.api.async_get_data()  # <-- Use the API method
            return data
        except (ClientError, Exception) as err:
            raise UpdateFailed(
                f"Error communicating with CumulusMX API: {err}") from err
