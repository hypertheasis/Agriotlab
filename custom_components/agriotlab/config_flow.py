from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN, CONF_LOCATION_NAME, CONF_LATITUDE, CONF_LONGITUDE


class AgriotConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(
                title=user_input[CONF_LOCATION_NAME],
                data=user_input,
            )

        schema = vol.Schema(
            {
                vol.Required(CONF_LOCATION_NAME): str,
                vol.Required(CONF_LATITUDE): vol.Coerce(float),
                vol.Required(CONF_LONGITUDE): vol.Coerce(float),
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
        )
