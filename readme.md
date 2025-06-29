

![Logo](https://raw.githubusercontent.com/JortvanSchijndel/FusionSolarPlus/refs/heads/master/branding/logo.png)

<p align="center">
<img alt="Total Downloads" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fanalytics.home-assistant.io%2Fcustom_integrations.json&query=%24.fusionsolarplus.total&logo=homeassistantcommunitystore&logoColor=%235c5c5c&label=Total%20Downloads&labelColor=%23ffffff&color=%234983FF&cacheSeconds=600&link=https%3A%2F%2Fmy.home-assistant.io%2Fredirect%2Fhacs_repository%2F%3Fowner%3DJortvanSchijndel%26repository%3DFusionSolarPlus%26category%3DIntegration">
<img alt="GitHub Release" src="https://img.shields.io/github/v/release/JortvanSchijndel/FusionSolarPlus?display_name=release&logo=V&logoColor=%235c5c5c&label=Latest%20Version&labelColor=%23ffffff&color=%234983FF&cacheSeconds=600&link=https%3A%2F%2Fgithub.com%2FJortvanSchijndel%2FFusionSolarPlus%2Freleases">
<img alt="Lint Workflow" src="https://img.shields.io/github/actions/workflow/status/JortvanSchijndel/FusionSolarPlus/lint.yml?logo=testcafe&logoColor=%235c5c5c&label=Lint%20Workflow&labelColor=%23ffffff&color=%234983FF&cacheSeconds=600&link=https%3A%2F%2Fgithub.com%2FJortvanSchijndel%2FFusionSolarPlus%2Factions%2Fworkflows%2Flint.yml">
<img alt="Hassfest & HACS Validation Workflow" src="https://img.shields.io/github/actions/workflow/status/JortvanSchijndel/FusionSolarPlus/validate.yml?logo=testcafe&logoColor=%235c5c5c&label=Hassfest%20%26%20HACS%20Validation%20Workflow&labelColor=%23ffffff&color=%234983FF&cacheSeconds=600&link=https%3A%2F%2Fgithub.com%2FJortvanSchijndel%2FFusionSolarPlus%2Factions%2Fworkflows%2Fvalidate.yml">
</p>

---

# FusionSolarPlus
This integration brings full FusionSolar support to Home Assistant, with separate entities for plants, inverters, and more. It authenticates using your FusionSolar username and password. No northbound API, OpenAPI, or kiosk URL required. I originally built it as a custom Python script that sent data via MQTT, but realizing others might want a Home Assistant integration with full entity support, I ported it with AI assistance into a proper integration for easier use.

## Setup
Click the button below and download the FusionSolarPlus integration.

<a href="https://my.home-assistant.io/redirect/hacs_repository/?owner=JortvanSchijndel&repository=FusionSolarPlus&category=Integration" target="_blank" rel="noreferrer noopener"><img src="https://my.home-assistant.io/badges/hacs_repository.svg" alt="Open your Home Assistant instance and open a repository inside the Home Assistant Community Store." /></a>

Once installed:

1. Restart Home Assistant and head over to **Settings » Devices & Services.**  
2. Click on **"Add Integration."**  
3. Search for **"FusionSolarPlus."**  
4. Enter your FusionSolar username and password.  
5. Select the device type you want to add, then choose the specific device.


> [!NOTE] 
> This integration currently only supports the endpoint:  
> [https://region01eu5.fusionsolar.huawei.com](https://region01eu5.fusionsolar.huawei.com)  
>  
> If you need a different endpoint, please [open an issue](https://github.com/JortvanSchijndel/FusionSolarPlus/issues).  
> To check your endpoint, log in to FusionSolar in your browser and check the URL.  
> A full list of endpoints can be found here:  
> [Huawei Support - Domain Name List of Management Systems](https://support.huawei.com/enterprise/en/doc/EDOC1100165054/dbeb5df3/domain-name-list-of-management-systems)

# Entities
> [!NOTE] 
> Currently, this integration only supports plants and inverters, as those are the devices I have access to.
> If you're missing support for a device (e.g., a battery), feel free to [open an issue](https://github.com/JortvanSchijndel/FusionSolarPlus/issues). I'll do my best to add compatibility even without direct access to the hardware.

## Plant
|Entity         |Unit       |
----------------|:------------:
|Current Power  |kW         |
|Today Energy   |kWh        |
|Montly Energy  |kWh        |
|Yearly Energy  |kWh        |
|Total Energy   |kWh        |
|Today Income   |[ISO 4217](https://en.wikipedia.org/wiki/ISO_4217#Active_codes) |

## Inverter
| Entity                 | Unit     |
|------------------------|:--------:|
| Current Active Power   | kW       |
| Daily Energy           | kWh      |
| Grid Frequency         | Hz       |
| Insulation Resistance  | MΩ       |
| Last Shutdown Time     | Datetime |
| Last Startup Time      | Datetime |
| Output Mode            | Text     |
| Phase A Current        | A        |
| Phase A Voltage        | V        |
| Phase B Current        | A        |
| Phase B Voltage        | V        |
| Phase C Current        | A        |
| Phase C Voltage        | V        |
| Power Factor           | Ratio    |
| Rated Power            | kW       |
| Reactive Power         | kvar     |
| Status                 | Text     |
| Temperature            | °C       |
| Total Energy Produced  | kWh      |

# Issues
If you encounter any problems while using the integration, please [open an issue](https://github.com/JortvanSchijndel/FusionSolarPlus/issues).
Be sure to include as much relevant information as possible, this helps with troubleshooting and speeds up the resolution process.


