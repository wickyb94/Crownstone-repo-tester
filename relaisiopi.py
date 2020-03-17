#!/usr/bin/env python
import RPi.GPIO as GPIO
from IOPi import IOPi
import time

bus = IOPi(0x21)
bus.set_port_direction(0, 0x00)
bus.set_port_direction(1, 0x00)
bus.write_port(0, 0xFF)
bus.write_port(1, 0xFF)

time.sleep(1)

for x in range (1,17):
    bus.write_pin(x, 0)
    time.sleep(0.5)
for x in range (1,17):
    bus.write_pin(x, 1)
    time.sleep(0.5)