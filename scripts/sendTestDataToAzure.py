import os
import asyncio
from azure.iot.device.aio import IoTHubDeviceClient

CONNECTION_STRING = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")
PAYLOAD = '{{"pm2": {pm2}, "pm10": {pm10}}}'

async def main():
    # Fetch the connection string from an environment variable
    # conn_str = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")

    # Create instance of the device client using the authentication provider
    device_client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    # Connect the device client.
    await device_client.connect()

    data = PAYLOAD.format(pm2=5, pm10=6)
    # message = Message(data)

    # Send a message to the IoT hub
    print(f"Sending message: {data}")
    await device_client.send_message(data)
    print("Message successfully sent")

    # Send a single message
    # print("Sending message...")
    # await device_client.send_message("This is a message that is being sent")

    # finally, shut down the client
    await device_client.shutdown()


if __name__ == "__main__":
    asyncio.run(main())

# import json
# import os
# import time
# import datetime
# import serial
# import redis
# # import aqi
# from azure.iot.device import Message
# from azure.iot.device.aio import IoTHubDeviceClient

# CONNECTION_STRING = os.environ.get('IOTHUB_DEVICE_CONNECTION_STRING')
# PAYLOAD = '{{"pm2": {pm2}, "pm10": {pm10}}}'

# print("Connecting to Azure IoT Hub...")
# print(CONNECTION_STRING)
# azureIoTClient = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

# data = PAYLOAD.format(pm2=5, pm10=6)
# message = Message(data)

# # Send a message to the IoT hub
# print(f"Sending message: {message}")
# azureIoTClient.send_message(message)

# print("Message successfully sent")