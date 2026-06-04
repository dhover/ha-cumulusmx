"""CumulusMX API client."""

import asyncio
import logging
from aiohttp import ClientError
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import (
    CONF_HOST,
    CONF_PORT,
    DEFAULT_WEBTAGS,
    EXTRA_WEBTAGS,
    SENSOR_API_URL,
    create_sensor_post_body,
)

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


async def _async_validate_connection(hass, user_input: dict) -> bool:
    """Validate that CumulusMX can be reached."""
    webtags = [*DEFAULT_WEBTAGS, *EXTRA_WEBTAGS]
    api = CumulusMXApi(
        hass,
        SENSOR_API_URL.format(
            host=user_input[CONF_HOST],
            port=user_input[CONF_PORT],
        ),
        create_sensor_post_body(webtags),
    )

    try:
        async with asyncio.timeout(10):
            await api.async_get_data()
    except (TimeoutError, ClientError, OSError, Exception):
        return False

    return True
