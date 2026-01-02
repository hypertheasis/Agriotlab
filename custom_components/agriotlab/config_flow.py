from homeassistant import config_entries
from homeassistant.core import callback

DOMAIN = "agriotlab"


class AgriotLabConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for AgriotLab."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Initial step."""
        if user_input is not None:
            return self.async_create_entry(
                title="AgriotLab",
                data={}
            )

        return self.async_show_form(
            step_id="user",
            data_schema=None,
        )
