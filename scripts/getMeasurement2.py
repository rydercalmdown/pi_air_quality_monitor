import serial, time

ser = serial.Serial('/dev/ttyUSB0')

while True:
	data = []
	for index in range(0,10):
		datum = ser.read()
		data.append(datum)

	pmtwofive = int.from_bytes(b''.join(data[2:4]), byteorder='little') / 10
	pmten = int.from_bytes(b''.join(data[4:6]), byteorder='little') / 10

	print(f"Data point: pm25 = {pmtwofive}  pm10 = {pmten}")
	time.sleep(10)
