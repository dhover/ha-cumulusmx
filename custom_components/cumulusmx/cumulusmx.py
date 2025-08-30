"""CumulusMX API client."""

import logging
from aiohttp import ClientError
from homeassistant.helpers.aiohttp_client import async_get_clientsession

_LOGGER = logging.getLogger(__name__)

class CumulusMXApi:
    """CumulusMX API client."""

    def __init__(self, hass, url, post_body):
        self.hass = hass
        self.url = url
        self.post_body = post_body

    async def async_get_data(self):
        """Fetch data from the CumulusMX API."""
        try:
            session = async_get_clientsession(self.hass)
            async with session.post(self.url, json=self.post_body, timeout=10) as response:
                response.raise_for_status()
                data = await response.json(content_type=None)
                _LOGGER.debug("Received data from CumulusMX: %s", data)
                return data
        except (ClientError, Exception) as err:
            _LOGGER.error("Error communicating with CumulusMX API: %s", err)
            raise
