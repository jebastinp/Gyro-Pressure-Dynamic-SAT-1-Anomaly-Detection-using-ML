from machine import Pin
from Sate.mq2 import MQ2
import utime
from Sat.assistant import dashboard

led = Pin(25,Pin.OUT)
sensor = MQ2(pinData = 26)

sensor.calibrate()

while True:
    Gas = sensor.readLPG()
    Smoke = sensor.readSmoke()
    Methane = sensor.readMethane()
    Hydrogen = sensor.readHydrogen()
    
    dashboard.sendAir(Smoke, Gas, Methane, Hydrogen)
    utime.sleep(0.5)


