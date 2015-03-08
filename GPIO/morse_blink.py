#!/usr/bin/env python3

import RPi.GPIO
import time
import sys
from morse import Morse

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(2,RPi.GPIO.OUT)

m = Morse()
m.dit(0.15) # set the time of a 'dit'

if not sys.argv:
    print( "Nada?" )
    print( sys.argv ) 
    exit(333)

def on():
    RPi.GPIO.output(2,True)
def off():
    RPi.GPIO.output(2,False)

for t in m.timing(m.translate(' '.join(sys.argv[1:]))):

    if t[0] == 'on':
        on()
    else:
        off()    
    time.sleep(t[1])

