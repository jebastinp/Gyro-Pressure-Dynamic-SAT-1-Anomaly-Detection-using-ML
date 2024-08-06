import machine
import utime
import uos

from Sate.mq2 import MQ2
from Sate.gyro import MPU6050
from Sate.pressure import *
from Sate.assistant import *

#i2c configuration
i2c = machine.I2C(0,scl=machine.Pin(1), sda=machine.Pin(0))
devices = i2c.scan()
if devices:
    print(devices)

#mq2 configuration
#sensor = MQ2(pinData = 26)
#sensor.calibrate()

#gyro configuration
mpu6050=MPU6050(i2c)

#pressure configuration
bmp280 = BMP280(i2c)
calibrate.pressure(bmp280)

#led configuration
led = machine.Pin(25, machine.Pin.OUT)
n = 0
#sensor calibration
while True:
    t=time.ticks_ms()/1000
    #bmp280 sensor
    Pressure = bmp280.pressure
    temperature = bmp280.temperature
    #MQ2 sensor
    #LPG = sensor.readLPG()
    #Smoke = sensor.readSmoke()
    #Methane = sensor.readMethane()
    #Hydrogen = sensor.readHydrogen()
    #MPU6050 sensor
    gx=round(mpu6050.gyro.x,2)
    gy=round(mpu6050.gyro.y,2)
    gz=round(mpu6050.gyro.z,2)
    ax=round(mpu6050.accel.x,2)
    ay=round(mpu6050.accel.y,2)
    az=round(mpu6050.accel.z,2)
    if n%2==0:
        led.on()
        print("Led on")
    else:
        led.off()
        print("Led off")
    #share to dashboard
    dashboard.sendWoair(Pressure, temperature, ax, ay, az, gx, gy, gz)
    #dashboard.sendAll(Pressure, temperature, Smoke, LPG, Methane, Hydrogen, ax, ay, az, gx, gy, gz)    
    utime.sleep(0.5)
    n=n+1
    
