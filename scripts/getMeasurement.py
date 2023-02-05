from sds011 import SDS011

port = "/dev/ttyUSB0"
sds = SDS011(port=port)
sds.set_working_period(rate=5)
meas = sds.read_measurement()

print(meas)


# print(sds)