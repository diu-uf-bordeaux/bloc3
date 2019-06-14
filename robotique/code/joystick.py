import time
import serial

# Ouverture de la ligne série 115200 bauds
port = serial.Serial('/dev/ttyUSB0', 115200)

while True:
    line = port.readline()
    parts = [float(x) for x in line.split(b' ')]
    x = parts[0]
    y = parts[1]

    print('x=%f, y=%f' % (x, y))
    