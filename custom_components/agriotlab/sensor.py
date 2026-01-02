from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities,
) -> None:
    async_add_entities([AgriotDummySensor(entry)])


class AgriotDummySensor(SensorEntity):
    def __init__(self, entry: ConfigEntry):
        self._attr_name = f"AgriotLab {entry.data['location_name']}"
        self._attr_unique_id = f"agriotlab_{entry.entry_id}"
        self._state = "ok"

    @property
    def native_value(self):
        return self._state
