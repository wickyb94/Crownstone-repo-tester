#!/usr/bin/env

"""An example that switches a Crownstone, and prints the r usage of all Crownstones."""

import time
from BluenetLib import Bluenet, BluenetEventBus, UsbTopics


# Create new instance of Bluenet
bluenet = Bluenet()

# Function that's called when the power usage is updated.
def showUartMessage(data):
    print("Received payload", data)

# Start up the USB bridge.
# Fill in the correct device, see the readme.
# For firmware versions below 2.1, add the parameter baudrate=38400
bluenet.initializeUSB("/dev/ttyUSB0")
bluenet._usbDev.setUartMode(3)
# Set up event listeners
BluenetEventBus.subscribe(UsbTopics.uartMessage, showUartMessage)

def uart(hello):
    bluenet.uartEcho(hello)
    time.sleep(0.2)
bluenet.stop()



