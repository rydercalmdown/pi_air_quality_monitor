# import json
# import os
# import time
# from sds011 import SDS011
# import redis

import json
import os
import time
import datetime
import serial
import redis
import aqi
from azure.iot.device import Message
from azure.iot.device.aio import IoTHubDeviceClient
import asyncio

CONNECTION_STRING = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")
PAYLOAD = '{{"pm2": {pm2}, "pm10": {pm10}}}'

redis_client = redis.StrictRedis(host=os.environ.get('REDIS_HOST'), port=6379, db=0)

# https://learn.microsoft.com/en-us/python/api/azure-iot-device/azure.iot.device.aio.iothubdeviceclient?view=azure-python
azureIoTClient = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

class AirQualityMonitor():

    # def __init__(self):
    #     self.sds = SDS011(port='/dev/ttyUSB0')
    #     self.sds.set_working_period(rate=1)

    def __init__(self):
        self.ser = serial.Serial('/dev/ttyUSB0')

    # def get_measurement(self):
    #     return {
    #         'time': int(time.time()),
    #         'measurement': self.sds.read_measurement(),
    #     }

    def get_measurement(self):
        self.data = []
        for index in range(0,10):
            datum = self.ser.read()
            self.data.append(datum)

        self.pmtwo = int.from_bytes(b''.join(self.data[2:4]), byteorder='little') / 10
        self.pmten = int.from_bytes(b''.join(self.data[4:6]), byteorder='little') / 10
        # myaqi = aqi.to_aqi([(aqi.POLLUTANT_PM25, str(self.pmtwo)),
        #                     (aqi.POLLUTANT_PM10, str(self.pmten))])
        # self.aqi = float(myaqi)

        self.meas = {
            "timestamp": datetime.datetime.now(),
            "pm2.5": self.pmtwo,
            "pm10": self.pmten,
            # "aqi": self.aqi,
        }
        return {
            'time': int(time.time()),
            'measurement': self.meas
        }

    def save_measurement_to_redis(self):
        """Saves measurement to redis db"""
        redis_client.lpush('measurements', json.dumps(self.get_measurement(), default=str))

    async def send_measurement_to_azure(self):
        """Sends measurement to Azure IoT Hub"""

        # self.data = []
        # for index in range(0,10):
        #     datum = self.ser.read()
        #     self.data.append(datum)

        # self.pmtwo = int.from_bytes(b''.join(self.data[2:4]), byteorder='little') / 10
        # self.pmten = int.from_bytes(b''.join(self.data[4:6]), byteorder='little') / 10

        # data = PAYLOAD.format(pm2=self.pmtwo, pm10=self.pmten)
        # message = Message(data)

        await azureIoTClient.send_message(self.get_last_n_measurements(2))

        # asyncio.create_task(ws.send(payload))

        # Send a message to the IoT hub
        # print(f"Sending message: {data}")

        # await azureIoTClient.send_message(json.dumps(self.get_measurement(), default=str))
        print("Message successfully sent")

    def get_last_n_measurements(self):
        """Returns the last n measurements in the list"""
        return [json.loads(x) for x in redis_client.lrange('measurements', 0, -1)]
