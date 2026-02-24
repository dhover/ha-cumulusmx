# CumulusMX Integration for Home Assistant

## Overview
The CumulusMX integration allows you to connect your CumulusMX weather station to Home Assistant, enabling you to monitor and control your weather data seamlessly.

## Installation

### GUI Installation (Recommended)
1. In Home Assistant, go to **Settings** > **Devices & Services**.
2. Click **+ Add Integration** and search for "CumulusMX".
3. Follow the on-screen instructions to complete the setup.

### Manual Installation
1. Download the CumulusMX integration files.
2. Place the `cumulusmx` folder in your Home Assistant `custom_components` directory.
3. Restart Home Assistant to recognize the new integration.

## Webtags

The integration supports the following webtags (sensor keys):

```
AirLinkPm1Out
AirLinkPm2p5Out
AirLinkPm2p5_1hrOut
AirLinkPm2p5_3hrOut
AirLinkPm2p5_24hrOut
AirLinkPm2p5_NowCastOut
AirLinkPm10Out
AirLinkPm10_1hrOut
AirLinkPm10_3hrOut
AirLinkPm10_24hrOut
AirLinkPm10_NowCastOut
AirLinkAqiPm2p5Out
AirLinkAqiPm2p5_1hrOut
AirLinkAqiPm2p5_3hrOut
AirLinkAqiPm2p5_24hrOut
AirLinkAqiPm2p5_NowCastOut
AirLinkAqiPm10Out
AirLinkAqiPm10_1hrOut
AirLinkAqiPm10_3hrOut
AirLinkAqiPm10_24hrOut
AirLinkAqiPm10_NowCastOut
AirLinkTempOut
AirLinkHumOut
avgbearing
bearing
build
dew
hum
inhum
intemp
LastRainTipISO
MulticastBadCnt
MulticastGoodCnt
MulticastGoodPct
press
ProgramUpTime
rfall
rrate
SolarRad
SystemUpTime
temp
timehhmmss
txbattery channel=1
txbattery channel=2
UV
version
wgust
wlatest
wspeed
```

## Usage
Once configured, the CumulusMX integration will create sensor entities in Home Assistant that represent various weather data points. You can view and use these sensors in your Home Assistant dashboard.

## Troubleshooting
If you encounter issues, check the Home Assistant logs for any error messages related to the CumulusMX integration. Ensure that your CumulusMX server is running and accessible from your Home Assistant instance.

## Contributing
If you would like to contribute to the CumulusMX integration, please fork the repository and submit a pull request with your changes.
