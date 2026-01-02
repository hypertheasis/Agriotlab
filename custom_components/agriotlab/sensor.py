"""AgriotLab basic sensor."""

from homeassistant.components.sensor import SensorEntity
from homeassistant.const import CONF_NAME

DOMAIN = "agriotlab"


async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([AgriotLabStatusSensor()])


class AgriotLabStatusSensor(SensorEntity):
    """Basic status sensor for AgriotLab."""

    _attr_name = "AgriotLab Status"
    _attr_unique_id = "agriotlab_status"
    _attr_icon = "mdi:sprout"

    @property
    def native_value(self):
        return "ready"
