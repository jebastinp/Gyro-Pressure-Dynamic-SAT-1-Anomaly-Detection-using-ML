import machine
import utime
#
trigger=machine.Pin(0,machine.Pin.OUT)
echo=machine.Pin(1,machine.Pin.IN,machine.Pin.PULL_DOWN)

buzzer=machine.Pin(2,machine.Pin.OUT)
ledg=machine.Pin(3,machine.Pin.OUT)
ledr=machine.Pin(15,machine.Pin.OUT)

while True:
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()

    while echo.value()==0:
        send=utime.ticks_us()

    while echo.value()==1:
        receive=utime.ticks_us()
        
    duration=receive-send

    distance=(duration*0.0343)/2
    print(distance)
    utime.sleep(0.2)
    
    if distance<25:
        buzzer.on()
        ledr.on()
        ledg.off()
        utime.sleep(0.1)
        
    else:
        ledg.on()
        ledr.off()
        buzzer.off()
        utime.sleep(0.1)
