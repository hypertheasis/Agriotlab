from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    data = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([AgriotStatusSensor(data)])


class AgriotStatusSensor(SensorEntity):
    _attr_name = "AgriotLab Status"
    _attr_icon = "mdi:sprout"

    def __init__(self, data: dict):
        self._data = data
        self._attr_unique_id = f"agriotlab_status_{data.get('location_name', 'default')}"

    @property
    def native_value(self):
        return "ready"
