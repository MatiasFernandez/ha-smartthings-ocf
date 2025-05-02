# ha-smartthings-ocf
A script to enhance the data Home Assistant's SmartThings integration retrieves from a Samsung OCF Refrigerator.

## Why is this needed?

As of May 1, 2025, the official Home Assistant SmartThings integration struggles with Samsung devices that report multiple components. As a result, not all stats are pulled into Home Assistant.

This script provides a quick and dirty way to fetch some of the missing stats, improving the monitoring of your refrigerator in Home Assistant.

## How does it work?

This tool consists of three parts:

1. A Python script that uses the access token from the official SmartThings integration to fetch the missing data from the SmartThings cloud.
2. A Home Assistant template sensor to store the fetched data as multiple attributes.
3. Additional template sensors to extract individual stats from the attributes and expose them as separate sensors.

The sensors reported by this script include:

- Current temperature of the cooler
- Current temperature of the freezer
- Target (setpoint) temperature of the cooler
- Target (setpoint) temperature of the freezer

## Requirements

This script depends on the official SmartThings integration, so you need to have it installed and configured.

You also need to find your `device_id` to set it in the `configuration.yaml`. To do this, use the "Download Statistics" option in the official SmartThings integration within Home Assistant and look for the `deviceId` key inside the `info` section.

## Limitations

This script is a quick solution for my personal needs. It has the following limitations:

- It doesn't provide detailed error reporting.
- It only fetches temperature-related stats.
- It supports only a single device.

I have only tested it with a Samsung RB50 refrigerator, so it may not work correctly with other models.

Additionally, I run Home Assistant in Container mode, so I can't guarantee compatibility with other installation methods.

I tested this with Home Assistant Core 2025.4.4

## How to use it

Follow these steps:

1. Copy the Python script into a folder named `scripts` within the config directory of your Home Assistant installation.
2. Copy the contents of `sample_configuration.yaml` into your `configuration.yaml` file.
3. Replace `YOUR_DEVICE_ID` in the `configuration.yaml` with your device's ID.
4. Restart Home Assistant and enjoy the enhanced monitoring.

## Need help?

If you encounter issues, feel free to create an issue. While I can't promise a solution, I'll do my best to help.