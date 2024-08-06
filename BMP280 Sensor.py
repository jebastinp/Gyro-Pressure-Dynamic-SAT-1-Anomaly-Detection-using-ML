import machine
import utime
from Sate.pressure import *
from Sate.assistant import *


i2c = machine.I2C(0,scl=machine.Pin(1),sda=machine.Pin(0))
bmp280 = BMP280(i2c)
calibrate.pressure(bmp280)
utime.sleep(2)

while True:
    pressure = bmp280.pressure
    temperature = bmp280.temperature
    dashboard.sendPressure(pressure, temperature)
    utime.sleep(1)