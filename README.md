# Raspberry Pi Air Quality Monitor
A simple air quality monitoring service for the Raspberry Pi.

## Installation
Clone the repository and run the following:
```bash
make install
```

## Running
To run, use the run command:
```bash
make run
```

## Architecture
This project uses python, flask, docker-compose and redis to create a simple web server to display the latest historical values from the sensor.

## Example Data
Some example data you can get from the sensor includes the following:

```json
{
    "device_id": 13358,
    "pm10": 10.8,
    "pm2.5": 4.8,
    "timestamp": "2021-06-16 22:12:13.887717"
}
```

The sensor reads two particulate matter (PM) values.

PM10 is a measure of particles less than 10 micrometers, whereas PM 2.5 is a measurement of finer particles, less than 2.5 micrometers.

Different particles are from different sources, and can be hazardous to different parts of the respiratory system.
