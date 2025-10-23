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

## Configuration
To configure the CumulusMX integration, add the following to your `configuration.yaml` file:

## Webtags

The integration supports the following webtags (sensor keys):

```
airlinkpm1out
airlinkpm2p5out
airlinkpm2p5_1hrout
airlinkpm2p5_3hrout
airlinkpm2p5_24hrout
airlinkpm2p5_nowcastout
airlinkpm10out
airlinkpm10_1hrout
airlinkpm10_3hrout
airlinkpm10_24hrout
airlinkpm10_nowcastout
airlinkaqipm2p5out
airlinkaqipm2p5_1hrout
airlinkaqipm2p5_3hrout
airlinkaqipm2p5_24hrout
airlinkaqipm2p5_nowcastout
airlinkaqipm10out
airlinkaqipm10_1hrout
airlinkaqipm10_3hrout
airlinkaqipm10_24hrout
airlinkaqipm10_nowcastout
airlinktempout
airlinkhumout
avgbearing
bearing
build
dew
hum
inhum
intemp
lastraintipiso
multicastbadcnt
multicastgoodcnt
multicastgoodpct
press
programuptime
rfall
rrate
systemuptime
temp
timehhmmss
txbattery channel=1
txbattery channel=2
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
