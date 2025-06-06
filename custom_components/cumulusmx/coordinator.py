from datetime import timedelta
import logging

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from aiohttp import ClientError
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import (
    DOMAIN,
    CONF_HOST,
    CONF_PORT,
    CONF_UPDATE_INTERVAL,
    SENSOR_API_URL,
    SENSOR_POST_BODY,
    DEFAULT_UPDATE_INTERVAL,
)

_LOGGER = logging.getLogger(__name__)


class CumulusMXCoordinator(DataUpdateCoordinator):
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry):
        self.hass = hass
        self.host = config_entry.data[CONF_HOST]
        self.port = config_entry.data[CONF_PORT]
        self.url = SENSOR_API_URL.format(host=self.host, port=self.port)
        self.post_body = SENSOR_POST_BODY
        update_interval = timedelta(seconds=config_entry.data.get(
            CONF_UPDATE_INTERVAL, DEFAULT_UPDATE_INTERVAL))

        super().__init__(
            hass,
            _LOGGER,
            name=f"{DOMAIN} Coordinator",
            update_interval=update_interval,
        )

    async def _async_update_data(self):
        try:
            session = async_get_clientsession(self.hass)
            async with session.post(self.url, data=self.post_body, timeout=10) as response:
                response.raise_for_status()
                data = await response.json(content_type=None)
                _LOGGER.debug("Received data from CumulusMX: %s", data)
                return data
        except (ClientError, Exception) as err:
            raise UpdateFailed(
                f"Error communicating with CumulusMX API: {err}") from err
