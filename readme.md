

![Logo](https://raw.githubusercontent.com/JortvanSchijndel/FusionSolarPlus/refs/heads/master/branding/logo.png)


# FusionSolarPlus
This integration brings full FusionSolar support to Home Assistant, with separate entities for plants, inverters, and more. It authenticates using your FusionSolar username and password—no northbound API, OpenAPI, or kiosk URL needed. I originally built it as a custom Python script that sent data via MQTT, but realizing the kiosk URL offers only limited entities and others might want a native Home Assistant integration with full entity support, I ported it with AI assistance into a proper integration for easier use.

## Setup

Currently, this integration is not available in HACS by default. To use it, you’ll need to add it as a custom repository:

1. Click the hamburger menu in the top-right corner of HACS.  
2. Click on **"Custom repositories."**  
3. Add the repository link: [https://github.com/JortvanSchijndel/FusionSolarPlus](https://github.com/JortvanSchijndel/FusionSolarPlus), select **"Integration"** as the type, and click **"Add."**  
4. Search in HACS for **"FusionSolarPlus."**  
5. In the bottom-right corner, select **"Install."**

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
If you encounter any problems while using the integration, please [open an issue.](https://github.com/JortvanSchijndel/FusionSolarPlus/issues).
Be sure to include as much relevant information as possible, this helps with troubleshooting and speeds up the resolution process.


