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
    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="CumulusMX", data=user_input)

        data_schema = vol.Schema({
            vol.Required(CONF_HOST, default=DEFAULT_HOST): str,
            vol.Required(CONF_PORT, default=DEFAULT_PORT): int,
            vol.Required(CONF_WEBTAGS, default=DEFAULT_WEBTAGS): str,
            vol.Optional(CONF_UPDATE_INTERVAL, default=DEFAULT_UPDATE_INTERVAL): int,
        })

        return self.async_show_form(
            step_id="user", data_schema=data_schema, errors=errors
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return CumulusMXOptionsFlowHandler(config_entry)


class CumulusMXOptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            result = self.async_create_entry(data=user_input)
            if self.hass:
                await self.hass.config_entries.async_reload(self.config_entry.entry_id)
            return result

        return self.async_show_form(
            step_id="init",
            data_schema=self.add_suggested_values_to_schema(
                OPTIONS_SCHEMA,
                {**self.config_entry.data, **self.config_entry.options}
            ),
        )
