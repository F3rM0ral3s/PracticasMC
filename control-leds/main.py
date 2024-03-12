from machine import Pin
from time import sleep

p16 = Pin(16, Pin.IN, Pin.PULL_DOWN)
p17 = Pin(17, Pin.IN, Pin.PULL_DOWN)
p18 = Pin(18, Pin.IN, Pin.PULL_DOWN)

r_led1 = Pin(8, Pin.OUT)
g_led1 = Pin(9, Pin.OUT)
o_led1 = Pin(10, Pin.OUT)
b_led1 = Pin(11, Pin.OUT)
b_led2 = Pin(12, Pin.OUT)
o_led2 = Pin(13, Pin.OUT)
g_led2 = Pin(14, Pin.OUT)
r_led2 = Pin(15, Pin.OUT)
leds = [0, 0, 0, 0, 0, 0, 0, 0]

def on_off():
    r_led1.value(1)
    g_led1.value(1)
    o_led1.value(1)
    b_led1.value(1)
    b_led2.value(1)
    o_led2.value(1)
    g_led2.value(1)
    r_led2.value(1)
    sleep(0.2)
    r_led1.value(0)
    g_led1.value(0)
    o_led1.value(0)
    b_led1.value(0)
    b_led2.value(0)
    o_led2.value(0)
    g_led2.value(0)
    r_led2.value(0)
    sleep(0.2)
    
def nibbles():
    r_led1.value(1)
    g_led1.value(1)
    o_led1.value(1)
    b_led1.value(1)
    b_led2.value(0)
    o_led2.value(0)
    g_led2.value(0)
    r_led2.value(0)
    sleep(0.2)
    r_led1.value(0)
    g_led1.value(0)
    o_led1.value(0)
    b_led1.value(0)
    b_led2.value(1)
    o_led2.value(1)
    g_led2.value(1)
    r_led2.value(1)
    sleep(0.2)
    
def half_nibbles_right():
    r_led1.value(1)
    g_led1.value(1)
    o_led1.value(0)
    b_led1.value(0)
    b_led2.value(0)
    o_led2.value(0)
    g_led2.value(0)
    r_led2.value(0)
    sleep(0.2)
    r_led1.value(0)
    g_led1.value(0)
    o_led1.value(1)
    b_led1.value(1)
    b_led2.value(0)
    o_led2.value(0)
    g_led2.value(0)
    r_led2.value(0)
    sleep(0.2)
    r_led1.value(0)
    g_led1.value(0)
    o_led1.value(0)
    b_led1.value(0)
    b_led2.value(1)
    o_led2.value(1)
    g_led2.value(0)
    r_led2.value(0)
    sleep(0.2)
    r_led1.value(0)
    g_led1.value(0)
    o_led1.value(0)
    b_led1.value(0)
    b_led2.value(0)
    o_led2.value(0)
    g_led2.value(1)
    r_led2.value(1)
    sleep(0.2)

def half_nibbles_left():
    r_led1.value(0)
    g_led1.value(0)
    o_led1.value(0)
    b_led1.value(0)
    b_led2.value(0)
    o_led2.value(0)
    g_led2.value(1)
    r_led2.value(1)
    sleep(0.2)
    r_led1.value(0)
    g_led1.value(0)
    o_led1.value(0)
    b_led1.value(0)
    b_led2.value(1)
    o_led2.value(1)
    g_led2.value(0)
    r_led2.value(0)
    sleep(0.2)
    r_led1.value(0)
    g_led1.value(0)
    o_led1.value(1)
    b_led1.value(1)
    b_led2.value(0)
    o_led2.value(0)
    g_led2.value(0)
    r_led2.value(0)
    sleep(0.2)
    r_led1.value(1)
    g_led1.value(1)
    o_led1.value(0)
    b_led1.value(0)
    b_led2.value(0)
    o_led2.value(0)
    g_led2.value(0)
    r_led2.value(0)
    sleep(0.2)
    
def shift(direction):
    for i in range(0, 8):
        if i == 0:
            leds[i] = int(not leds[i])
            leds[7] = 0
            sleep(0.2)
        else:
            leds[i] = int(not leds[i])
            leds[i-1] = int(not leds[i-1])
            sleep(0.2)
        # Right
        if direction == 0:
            r_led1.value(leds[0])
            g_led1.value(leds[1])
            o_led1.value(leds[2])
            b_led1.value(leds[3])
            b_led2.value(leds[4])
            o_led2.value(leds[5])
            g_led2.value(leds[6])
            r_led2.value(leds[7])
        # Left
        else:
            r_led1.value(leds[7])
            g_led1.value(leds[6])
            o_led1.value(leds[5])
            b_led1.value(leds[4])
            b_led2.value(leds[3])
            o_led2.value(leds[2])
            g_led2.value(leds[1])
            r_led2.value(leds[0])

def zig_zag():
    for i in range(0, 8):
        if i == 0:
            leds[i] = int(not leds[i])
            leds[7] = 0
        else:
            leds[i] = int(not leds[i])
            leds[i-1] = int(not leds[i-1])
            sleep(0.2)
        # Right
        r_led1.value(leds[0])
        g_led1.value(leds[1])
        o_led1.value(leds[2])
        b_led1.value(leds[3])
        b_led2.value(leds[4])
        o_led2.value(leds[5])
        g_led2.value(leds[6])
        r_led2.value(leds[7])
        
    for i in range(0, 8):
        if i == 0:
            leds[i] = int(not leds[i])
            leds[7] = 0
        else:
            leds[i] = int(not leds[i])
            leds[i-1] = int(not leds[i-1])
            sleep(0.2)
        # Right
        r_led1.value(leds[7])
        g_led1.value(leds[6])
        o_led1.value(leds[5])
        b_led1.value(leds[4])
        b_led2.value(leds[3])
        o_led2.value(leds[2])
        g_led2.value(leds[1])
        r_led2.value(leds[0])

while True:
    if p16.value() == 0 and p17.value() == 0 and p18.value() == 0:
        r_led1.value(0)
        g_led1.value(0)
        o_led1.value(0)
        b_led1.value(0)
        b_led2.value(0)
        o_led2.value(0)
        g_led2.value(0)
        r_led2.value(0)
    elif p16.value() == 0 and p17.value() == 0 and p18.value() == 1:
        on_off()
    elif p16.value() == 0 and p17.value() == 1 and p18.value() == 0:
        nibbles()
    elif p16.value() == 0 and p17.value() == 1 and p18.value() == 1:
        half_nibbles_right()
    elif p16.value() == 1 and p17.value() == 0 and p18.value() == 0:
        half_nibbles_left()
    elif p16.value() == 1 and p17.value() == 0 and p18.value() == 1:
        shift(0)
    elif p16.value() == 1 and p17.value() == 1 and p18.value() == 0:
        shift(1)
    elif p16.value() == 1 and p17.value() == 1 and p18.value() == 1:
        zig_zag()