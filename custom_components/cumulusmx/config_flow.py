"""Config flow for CumulusMX integration."""

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from .const import (
    DOMAIN, CONF_HOST, CONF_PORT, CONF_WEBTAGS, CONF_UPDATE_INTERVAL,
    DEFAULT_HOST, DEFAULT_PORT, DEFAULT_WEBTAGS, DEFAULT_UPDATE_INTERVAL
)

OPTIONS_SCHEMA = vol.Schema({
    vol.Required(CONF_HOST, default=DEFAULT_HOST): str,
    vol.Required(CONF_PORT, default=DEFAULT_PORT): int,
    vol.Required(CONF_WEBTAGS, default=DEFAULT_WEBTAGS): str,
    vol.Optional(CONF_UPDATE_INTERVAL, default=DEFAULT_UPDATE_INTERVAL): int,
})


class CumulusMXConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a CumulusMX config flow."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""

        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="CumulusMX", data=user_input)

        return self.async_show_form(
            step_id="user", data_schema=OPTIONS_SCHEMA, errors=errors
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
            return self.async_create_entry(data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=self.add_suggested_values_to_schema(
                OPTIONS_SCHEMA,
                {**self.config_entry.data, **self.config_entry.options}
            ),
        )
