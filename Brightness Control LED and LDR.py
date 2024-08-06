import machine
import utime

ldr=machine.ADC(machine.Pin(27))
led=machine.Pin(5,machine.Pin.OUT)
#led0=machine.Pin(1,machine.Pin.OUT)

while True:
    utime.sleep(0.5)
    value=ldr.read_u16()
    print(value*0.000056)
    Value=value*0.000056
    if Value>2:
        led.on()
        utime.sleep(0.5)
    else:
        led.off()
        utime.sleep(0.5)
    
    
