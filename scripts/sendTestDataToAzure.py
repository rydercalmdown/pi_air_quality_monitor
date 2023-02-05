import json
import os
import time
import datetime
import serial
import redis
# import aqi
from azure.iot.device import Message
from azure.iot.device.aio import IoTHubDeviceClient

CONNECTION_STRING = os.environ.get('AzureConnectionString')
PAYLOAD = '{{"pm2": {pm2}, "pm10": {pm10}}}'

print("Connecting to Azure IoT Hub...")
print(CONNECTION_STRING)
azureIoTClient = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

data = PAYLOAD.format(pm2=5, pm10=6)
message = Message(data)

# Send a message to the IoT hub
print(f"Sending message: {message}")
azureIoTClient.send_message(message)

print("Message successfully sent")