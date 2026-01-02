from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.config_entries import ConfigEntry

DOMAIN = "agriotlab"


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    async_add_entities(
        [
            AgriotLabAirTemperatureSensor(hass),
            AgriotLabWarmCropSowingSensor(hass),
        ]
    )


class AgriotLabBaseSensor(SensorEntity):
    """Base class for AgriotLab sensors."""

    should_poll = True

    def __init__(self, hass: HomeAssistant):
        self.hass = hass


class AgriotLabAirTemperatureSensor(AgriotLabBaseSensor):
    _attr_name = "AgriotLab Air Temperature"
    _attr_unique_id = "agriotlab_air_temperature"
    _attr_unit_of_measurement = "°C"
    _attr_device_class = "temperature"

    @property
    def native_value(self):
        state = self.hass.states.get("weather.athena_spiti")
        if not state:
            return None
        return state.attributes.get("temperature")


class AgriotLabWarmCropSowingSensor(AgriotLabBaseSensor):
    _attr_name = "AgriotLab Warm Crop Sowing Status"
    _attr_unique_id = "agriotlab_warm_crop_sowing"

    @property
    def
