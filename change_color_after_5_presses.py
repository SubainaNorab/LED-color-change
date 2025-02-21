from machine import Pin
from neopixel import NeoPixel
import time

btn =Pin(0, Pin.IN, Pin.PULL_UP)    # same pin for physical esp32 s3 built in Boot buton
pin = Pin(33, Pin.OUT)              # set 48 for your physical esp32 s3  
neo = NeoPixel(pin, 1)              # create NeoPixel driver  for 1 pixel



i=0
count=0
def btn_press(pin):
    global count, i 
    if(btn.value()==0): # solved debounce issue
        time.sleep(.1)
        if(btn.value()==0):
            count=count+1
            print(count)
            if (count==5):
                count=0  
                i=(i+90)%256 #ensuring numbers in limit
                j=(i+85)%256
                k=(i+175)%256
                neo[0]=(i,j,k)
                neo.write()
                time.sleep(.4)


btn.irq(trigger=Pin.IRQ_FALLING,handler=btn_press) #interrupt

while True:
    while(btn.value()==1):          # flashing of neopixel stopped when button is in pressed status
        continue