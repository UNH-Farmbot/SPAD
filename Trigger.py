





import serial
from time import sleep
port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=None)

while True:
    pin = input("").strip()
    port.write(str.encode(pin))
    sleep(0.1)
