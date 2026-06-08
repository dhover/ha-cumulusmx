# CumulusMX Integration for Home Assistant

## Overview
The CumulusMX integration connects a CumulusMX weather station to Home Assistant using the CumulusMX local API. It exposes weather, system and AirLink sensor data as Home Assistant entities.

## Features
- Local polling integration for CumulusMX API data
- Configurable host and port for your CumulusMX server
- Selectable webtags to control which sensors are exposed
- Sensor entities for weather, system diagnostics, and AirLink data
- Optional update entity for checking CumulusMX releases from GitHub

## Requirements
- Home Assistant with support for custom integrations
- Running CumulusMX instance reachable from Home Assistant
- CumulusMX HTTP API enabled and accessible via host + port

## Installation

### Manual Installation
1. Download the repository or integration files.
2. Copy the `cumulusmx` folder into your Home Assistant `custom_components` directory.
3. Restart Home Assistant.
4. Add the integration from Home Assistant UI.

### HACS Installation
This integration can also be installed through HACS if you add this repository as a custom repository.

## Setup
1. In Home Assistant, go to **Settings** > **Devices & Services**.
2. Click **+ Add Integration** and search for **CumulusMX**.
3. Enter your CumulusMX host and port.
   - Default host placeholder: `192.168.x.x`
   - Default port: `8998`
4. Save and wait for the integration to set up.

## Configuration Options
After adding the integration, you can customize which webtags are exposed as sensors:
- Open the integration in **Devices & Services**
- Click **Options**
- Select the webtags you want to enable

If no tags are selected, the integration will fall back to a default set of common weather values.

## Supported webtags
The integration supports the following webtag names:

```
temp
hum
dew
heatindex
press
rfall
rrate
wgust
wspeed
wlatest
wdir
currentwdir
bearing
avgbearing
LastRainTipISO
ProgramUpTime
SystemUpTime
timehhmmss
AirLinkPm1Out
AirLinkPm2p5Out
AirLinkPm2p5_1hrOut
AirLinkPm2p5_3hrOut
AirLinkPm2p5_24hrOut
AirLinkPm2p5_NowcastOut
AirLinkPm10Out
AirLinkPm10_1hrOut
AirLinkPm10_3hrOut
AirLinkPm10_24hrOut
AirLinkPm10_NowcastOut
AirLinkAqiPm2p5Out
AirLinkAqiPm2p5_1hrOut
AirLinkAqiPm2p5_3hrOut
AirLinkAqiPm2p5_24hrOut
AirLinkAqiPm2p5_NowcastOut
AirLinkAqiPm10Out
AirLinkAqiPm10_1hrOut
AirLinkAqiPm10_3hrOut
AirLinkAqiPm10_24hrOut
AirLinkAqiPm10_NowcastOut
AirLinkHumOut
AirLinkTempOut
build
MulticastBadCnt
MulticastGoodCnt
MulticastGoodPct
txbattery channel=1
txbattery channel=2
version
intemp
inhum
SolarRad
UV
```

These tags map to weather, system, and AirLink sensor entities in Home Assistant.

## Entities
The integration creates entities for:
- Weather sensors (temperature, humidity, pressure, wind, rainfall, UV, solar radiation, etc.)
- System diagnostics (uptime, build, version, packet counts, battery status)
- AirLink sensors (PM, AQI, temperature, humidity)
- Update entity for `CumulusMX Hub` to check latest release info

### Example sensor groups
- `Temperature`
- `Humidity`
- `Wind Speed`
- `Rainfall`
- `Pressure`
- `Solar Radiation`
- `Version`
- `Uptime`

## Troubleshooting
- Verify your CumulusMX server is running and reachable from Home Assistant.
- Confirm the host and port are correct.
- Check Home Assistant logs for `cumulusmx` errors.
- If the integration fails to connect, make sure the CumulusMX API endpoint is accessible.

## Contributing
Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with your changes.

## Support
- Repository: https://github.com/dhover/ha-cumulusmx
- Issues: https://github.com/dhover/ha-cumulusmx/issues
