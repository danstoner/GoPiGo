#!/usr/bin/env python
# This example is to control the LED's on a GoPiGo

from gopigo import *
import sys
import time

# We wrap the loop with try/except in order to make sure that we turn off the
# LEDs when the script is interrupted with ctrl-c
try:
        while True:
                print "ON"
                led_on(LED_L)
                led_on(LED_R)
                time.sleep(.5)

                print "OFF"
                led_off(LED_L)
                led_off(LED_R)
                time.sleep(.5)
except KeyboardInterrupt:
        led_off(LED_L)
        led_off(LED_R)
        raise SystemExit

