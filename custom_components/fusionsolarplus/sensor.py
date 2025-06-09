import logging
from datetime import timedelta

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorStateClass,
    SensorEntity,
)
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
    CoordinatorEntity,
)

from . import DOMAIN

_LOGGER = logging.getLogger(__name__)

# Currency (33 does not exist fsr)
CURRENCY_MAP = {
    1: "CNY",
    2: "USD",
    3: "JPY",
    4: "EUR",
    5: "GBP",
    6: "INR",
    7: "AUD",
    8: "LYD",
    9: "ZAR",
    10: "EGP",
    11: "ARS",
    12: "TRY",
    13: "MXN",
    14: "BRL",
    15: "PESETA",
    16: "CAD",
    17: "KRW",
    18: "MAD",
    19: "CLP",
    20: "PKR",
    21: "SAR",
    22: "THB",
    23: "MYR",
    24: "SGD",
    25: "VND",
    26: "PHP",
    27: "HKD",
    28: "PLN",
    29: "CHF",
    30: "TWD",
    31: "HUF",
    32: "TRY",
    34: "UAH",
    35: "NZD",
    36: "IDR",
    37: "GTQ",
    38: "HNL",
    39: "SVC",
    40: "PAB",
    41: "DOB",
    42: "VEF",
    43: "COP",
    44: "PEN",
    45: "BOB",
    46: "DKK",
    47: "NOK",
    48: "SEK",
    49: "KZT",
    50: "UZS",
}


# Device & state classes: https://developers.home-assistant.io/docs/core/entity/sensor/

#
# Define Signals from the API (entities)
#
INVERTER_SIGNALS = [
    {"id": 10025, "name": "Inverter status", "unit": "", "custom_name": "Status"},
    {"id": 10020, "name": "Power factor", "unit": "", "custom_name": "Power Factor"},
    {"id": 21029, "name": "Output mode", "unit": "", "custom_name": "Output Mode"},
    {
        "id": 10027,
        "name": "Inverter startup time",
        "unit": "",
        "custom_name": "Last Startup Time",
    },
    {
        "id": 10028,
        "name": "Inverter shutdown time",
        "unit": "",
        "custom_name": "Last Shutdown Time",
    },
    {
        "id": 10032,
        "name": "Daily energy",
        "unit": "kWh",
        "custom_name": "Daily Energy",
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL,
    },
    {
        "id": 10029,
        "name": "Cumulative energy",
        "unit": "kWh",
        "custom_name": "Total Energy Produced",
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL_INCREASING,
    },
    {
        "id": 10018,
        "name": "Active power",
        "unit": "kW",
        "custom_name": "Current Active Power",
        "device_class": SensorDeviceClass.POWER,
        "state_class": SensorStateClass.MEASUREMENT,
    },
    {
        "id": 10019,
        "name": "Output reactive power",
        "unit": "kvar",
        "custom_name": "Reactive Power",
        "device_class": SensorDeviceClass.POWER,
        "state_class": SensorStateClass.MEASUREMENT,
    },
    {
        "id": 10006,
        "name": "Inverter rated power",
        "unit": "kW",
        "custom_name": "Rated Power",
        "device_class": SensorDeviceClass.POWER,
        "state_class": SensorStateClass.MEASUREMENT,
    },
    {
        "id": 10021,
        "name": "Grid frequency",
        "unit": "Hz",
        "custom_name": "Grid Frequency",
        "device_class": SensorDeviceClass.FREQUENCY,
        "state_class": SensorStateClass.MEASUREMENT,
    },
    {
        "id": 10014,
        "name": "Grid phase A current",
        "unit": "A",
        "custom_name": "Phase A Current",
        "device_class": SensorDeviceClass.CURRENT,
        "state_class": SensorStateClass.MEASUREMENT,
    },
    {
        "id": 10015,
        "name": "Grid phase B current",
        "unit": "A",
        "custom_name": "Phase B Current",
        "device_class": SensorDeviceClass.CURRENT,
        "state_class": SensorStateClass.MEASUREMENT,
    },
    {
        "id": 10016,
        "name": "Grid phase C current",
        "unit": "A",
        "custom_name": "Phase C Current",
        "device_class": SensorDeviceClass.CURRENT,
        "state_class": SensorStateClass.MEASUREMENT,
    },
    {
        "id": 10011,
        "name": "Phase A voltage",
        "unit": "V",
        "custom_name": "Phase A Voltage",
        "device_class": SensorDeviceClass.VOLTAGE,
        "state_class": SensorStateClass.MEASUREMENT,
    },
    {
        "id": 10012,
        "name": "Phase B voltage",
        "unit": "V",
        "custom_name": "Phase B Voltage",
        "device_class": SensorDeviceClass.VOLTAGE,
        "state_class": SensorStateClass.MEASUREMENT,
    },
    {
        "id": 10013,
        "name": "Phase C voltage",
        "unit": "V",
        "custom_name": "Phase C Voltage",
        "device_class": SensorDeviceClass.VOLTAGE,
        "state_class": SensorStateClass.MEASUREMENT,
    },
    {
        "id": 10023,
        "name": "Internal temperature",
        "unit": "°C",
        "custom_name": "Temperature",
        "device_class": SensorDeviceClass.TEMPERATURE,
        "state_class": SensorStateClass.MEASUREMENT,
    },
    {
        "id": 10024,
        "name": "Insulation resistance",
        "unit": "MΩ",
        "custom_name": "Insulation Resistance",
    },
]

PLANT_SIGNALS = [
    {
        "key": "monthEnergy",
        "name": "Monthly Energy",
        "unit": "kWh",
        "custom_name": "Monthly Energy",
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL,
    },
    {
        "key": "cumulativeEnergy",
        "name": "Cumulative Energy",
        "unit": "kWh",
        "custom_name": "Total Energy",
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL_INCREASING,
    },
    {
        "key": "currentPower",
        "name": "Current Power",
        "unit": "kW",
        "custom_name": "Current Power",
        "device_class": SensorDeviceClass.POWER,
        "state_class": SensorStateClass.MEASUREMENT,
    },
    {
        "key": "dailyIncome",
        "name": "Daily Income",
        "unit": "",
        "custom_name": "Today Income",
        "device_class": SensorDeviceClass.MONETARY,
        "state_class": SensorStateClass.TOTAL,
    },
    {
        "key": "dailyEnergy",
        "name": "Daily Energy",
        "unit": "kWh",
        "custom_name": "Today Energy",
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL,
    },
    {
        "key": "yearEnergy",
        "name": "Yearly Energy",
        "unit": "kWh",
        "custom_name": "Yearly Energy",
        "device_class": SensorDeviceClass.ENERGY,
        "state_class": SensorStateClass.TOTAL,
    },
]


async def async_setup_entry(hass, entry, async_add_entities):
    device_id = entry.data["device_id"]
    device_name = entry.data["device_name"]
    device_type = entry.data["device_type"]

    device_info = {
        "identifiers": {(DOMAIN, device_name)},
        "manufacturer": "FusionSolar",
        "name": device_name,
        "model": device_type,
    }
    #
    # API for Inverter
    #
    if device_type == "Inverter":

        async def async_get_data():
            client = hass.data[DOMAIN][entry.entry_id]
            try:
                return await hass.async_add_executor_job(
                    client.get_real_time_data, device_id
                )
            except Exception as err:
                _LOGGER.error("Error fetching FusionSolar Inverter data: %s", err)
                raise UpdateFailed(f"Error fetching data: {err}")

        signals = INVERTER_SIGNALS
        entity_class = FusionSolarInverterSensor
    #
    # API for Plant
    #
    elif device_type == "Plant":

        async def async_get_data():
            client = hass.data[DOMAIN][entry.entry_id]
            try:
                return await hass.async_add_executor_job(
                    client.get_current_plant_data, device_id
                )
            except Exception as err:
                _LOGGER.error("Error fetching FusionSolar Plant data: %s", err)
                raise UpdateFailed(f"Error fetching data: {err}")

        signals = PLANT_SIGNALS
        entity_class = FusionSolarPlantSensor

    else:
        _LOGGER.error("Unsupported device type: %s", device_type)
        return

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name=f"{device_name} FusionSolar Data",
        update_method=async_get_data,
        update_interval=timedelta(seconds=15),
    )

    await coordinator.async_config_entry_first_refresh()

    entities = []
    for signal in signals:
        if device_type == "Inverter":
            entities.append(
                entity_class(
                    coordinator,
                    signal["id"],
                    signal.get("custom_name", signal["name"]),
                    signal["unit"],
                    device_info,
                    signal.get("device_class"),
                    signal.get("state_class"),
                )
            )
        elif device_type == "Plant":
            entities.append(
                entity_class(
                    coordinator,
                    signal["key"],
                    signal.get("custom_name", signal["name"]),
                    signal["unit"],
                    device_info,
                    signal.get("device_class"),
                    signal.get("state_class"),
                )
            )

    async_add_entities(entities)


#
#   Inverter
#


class FusionSolarInverterSensor(CoordinatorEntity, SensorEntity):
    def __init__(
        self,
        coordinator,
        signal_id,
        name,
        unit,
        device_info,
        device_class=None,
        state_class=None,
    ):
        super().__init__(coordinator)
        self._signal_id = signal_id
        self._attr_name = name
        self._attr_native_unit_of_measurement = unit
        self._attr_device_info = device_info
        self._attr_unique_id = f"{list(device_info['identifiers'])[0][1]}_{signal_id}"
        self._attr_device_class = device_class
        self._attr_state_class = state_class

    @property
    def state(self):
        data = self.coordinator.data
        if not data:
            return None
        for group in data.get("data", []):
            if "signals" in group:
                for signal in group["signals"]:
                    if signal["id"] == self._signal_id:
                        if signal.get("unit"):
                            try:
                                return float(signal.get("value"))
                            except (TypeError, ValueError):
                                return None
                        else:
                            return signal.get("value")
        return None

    @property
    def available(self):
        return (
            self.coordinator.last_update_success and self.coordinator.data is not None
        )


#
#   Plant
#


class FusionSolarPlantSensor(CoordinatorEntity, SensorEntity):
    def __init__(
        self,
        coordinator,
        key,
        name,
        unit,
        device_info,
        device_class=None,
        state_class=None,
    ):
        super().__init__(coordinator)
        self._key = key
        self._attr_name = name
        self._base_unit = unit
        self._attr_device_info = device_info
        self._attr_unique_id = f"{list(device_info['identifiers'])[0][1]}_{key}"
        self._attr_device_class = device_class
        self._attr_state_class = state_class

    @property
    def native_unit_of_measurement(self):
        # set currency unit dynamically from api
        if self._key == "dailyIncome":
            data = self.coordinator.data
            if data:
                currency_num = data.get("currency")
                if currency_num:
                    return CURRENCY_MAP.get(currency_num, str(currency_num))
        return self._base_unit

    @property
    def state(self):
        data = self.coordinator.data
        if not data:
            return None
        value = data.get(self._key)
        if value is None:
            return None
        if self.native_unit_of_measurement:
            try:
                return float(value)
            except (TypeError, ValueError):
                return None
        else:
            return value

    @property
    def available(self):
        return (
            self.coordinator.last_update_success and self.coordinator.data is not None
        )
