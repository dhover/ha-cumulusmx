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

```yaml
cumulusmx:
  host: YOUR_CUMULUSMX_HOST
  port: YOUR_CUMULUSMX_PORT
  update interval: YOUR_UPDATE_INTERVAL
```

Replace `YOUR_CUMULUSMX_HOST` and `YOUR_CUMULUSMX_PORT` with the appropriate values for your setup.

## Usage
Once configured, the CumulusMX integration will create sensor entities in Home Assistant that represent various weather data points. You can view and use these sensors in your Home Assistant dashboard.

## Troubleshooting
If you encounter issues, check the Home Assistant logs for any error messages related to the CumulusMX integration. Ensure that your CumulusMX server is running and accessible from your Home Assistant instance.

## Contributing
If you would like to contribute to the CumulusMX integration, please fork the repository and submit a pull request with your changes.