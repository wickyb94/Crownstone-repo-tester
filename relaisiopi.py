#!/usr/bin/env pythonimport RPi.GPIO as GPIO
from IOPi import IOPi
import time

#setting up the busses of the IO-extenssion board to control the relay module
bus = IOPi(0x21)
bus.set_port_direction(0, 0x00)
bus.set_port_direction(1, 0x00)
bus.write_port(0, 0xFF)
bus.write_port(1, 0xFF)

#a test code where all the 16 relays will go on and off
'''
for x in range (1,17):
    bus.write_pin(x, 0)
    time.sleep(0.5)
for x in range (1,17):
    bus.write_pin(x, 1)
    time.sleep(0.5)
'''
