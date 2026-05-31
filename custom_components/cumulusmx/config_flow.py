"""Config flow for CumulusMX integration."""

import asyncio

from aiohttp import ClientError
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers import selector
from homeassistant.core import callback
from .cumulusmx import CumulusMXApi
from .const import (
    DOMAIN, CONF_HOST, CONF_PORT, CONF_WEBTAGS,
    DEFAULT_HOST, DEFAULT_PORT, DEFAULT_WEBTAGS, ALL_WEBTAG_OPTIONS,
    EXTRA_WEBTAGS, SENSOR_API_URL, create_sensor_post_body,
    normalize_configurable_webtags,
)

def _build_options_schema() -> vol.Schema:
    return vol.Schema({
        vol.Required(CONF_WEBTAGS, default=DEFAULT_WEBTAGS): selector.SelectSelector(
            selector.SelectSelectorConfig(
                options=ALL_WEBTAG_OPTIONS,
                multiple=True,
                custom_value=False,
                mode=selector.SelectSelectorMode.LIST,
            )
        ),
    })


def _build_connection_schema() -> vol.Schema:
    return vol.Schema({
        vol.Required(CONF_HOST, default=DEFAULT_HOST): str,
        vol.Required(CONF_PORT, default=DEFAULT_PORT): int,
    })


def _build_entry_title(user_input: dict) -> str:
    """Build the config entry title."""
    return f"{user_input[CONF_HOST]}:{user_input[CONF_PORT]}"


def _connection_error_message(hass) -> str:
    """Return a user-facing connection error message."""
    if hass.config.language and hass.config.language.lower().startswith("nl"):
        return "Kan geen verbinding maken met CumulusMX. Controleer de host en poort."
    return "Failed to connect to CumulusMX. Check the host and port."


def _reconfigure_success_message(hass) -> str:
    """Return a user-facing reconfigure success message."""
    if hass.config.language and hass.config.language.lower().startswith("nl"):
        return "CumulusMX is opnieuw geconfigureerd."
    return "CumulusMX has been reconfigured."


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


class CumulusMXConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a CumulusMX config flow."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""

        errors = {}
        if user_input is not None:
            if not await _async_validate_connection(self.hass, user_input):
                errors["base"] = _connection_error_message(self.hass)
                return self.async_show_form(
                    step_id="user",
                    data_schema=self.add_suggested_values_to_schema(
                        _build_connection_schema(),
                        user_input,
                    ),
                    errors=errors,
                )

            user_input = {
                **user_input,
                CONF_WEBTAGS: DEFAULT_WEBTAGS,
            }
            return self.async_create_entry(
                title=_build_entry_title(user_input),
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=_build_connection_schema(),
            errors=errors,
        )

    async def async_step_reconfigure(self, user_input=None):
        """Handle reconfiguration of connection settings."""
        entry = self._get_reconfigure_entry()
        errors = {}

        if user_input is not None:
            if not await _async_validate_connection(self.hass, user_input):
                errors["base"] = _connection_error_message(self.hass)
                return self.async_show_form(
                    step_id="reconfigure",
                    data_schema=self.add_suggested_values_to_schema(
                        _build_connection_schema(),
                        user_input,
                    ),
                    errors=errors,
                )

            data = {
                **entry.data,
                CONF_HOST: user_input[CONF_HOST],
                CONF_PORT: user_input[CONF_PORT],
            }
            options = dict(entry.options)
            options.pop(CONF_HOST, None)
            options.pop(CONF_PORT, None)

            self.hass.config_entries.async_update_entry(
                entry,
                title=_build_entry_title(data),
                data=data,
                options=options,
            )
            await self.hass.config_entries.async_reload(entry.entry_id)
            return self.async_abort(reason=_reconfigure_success_message(self.hass))

        suggested_values = {
            CONF_HOST: entry.data.get(
                CONF_HOST, entry.options.get(CONF_HOST, DEFAULT_HOST)
            ),
            CONF_PORT: entry.data.get(
                CONF_PORT, entry.options.get(CONF_PORT, DEFAULT_PORT)
            ),
        }
        return self.async_show_form(
            step_id="reconfigure",
            data_schema=self.add_suggested_values_to_schema(
                _build_connection_schema(),
                suggested_values,
            ),
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get the options flow handler."""

        return CumulusMXOptionsFlowHandler()


class CumulusMXOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle CumulusMX options flow."""

    async def async_step_init(self, user_input=None):
        """Manage the options."""

        if user_input is not None:
            user_input[CONF_WEBTAGS] = normalize_configurable_webtags(
                user_input.get(CONF_WEBTAGS, DEFAULT_WEBTAGS)
            )
            if not user_input[CONF_WEBTAGS]:
                user_input[CONF_WEBTAGS] = DEFAULT_WEBTAGS
            return self.async_create_entry(data=user_input)

        suggested_values = self._get_suggested_values()
        return self.async_show_form(
            step_id="init",
            data_schema=self.add_suggested_values_to_schema(
                _build_options_schema(),
                suggested_values,
            ),
        )

    def _get_suggested_values(self) -> dict:
        values = {**self.config_entry.data, **self.config_entry.options}
        values[CONF_WEBTAGS] = normalize_configurable_webtags(
            values.get(CONF_WEBTAGS, DEFAULT_WEBTAGS)
        )
        if not values[CONF_WEBTAGS]:
            values[CONF_WEBTAGS] = DEFAULT_WEBTAGS
        return values
