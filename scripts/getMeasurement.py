from sds011 import SDS011

port = "/dev/ttyUSB0"
sds = SDS011(port=port)

print(sds)