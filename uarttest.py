#!/usr/bin/env python3


import time
from BluenetLib import Bluenet, BluenetEventBus, UsbTopics
from BluenetLib.lib.topics.DevTopics import DevTopics

bluenet = Bluenet()

def uartecho(HelloWorld):
    def showUartMessage(data):
        print("Received payload", data)
    echo = BluenetEventBus.subscribe(UsbTopics.uartMessage, showUartMessage)
    bluenet.uartEcho(HelloWorld)
    time.sleep(0.2)
    bluenet.uartEcho(HelloWorld)
    time.sleep(0.2)
    BluenetEventBus.unsubscribe(echo)


def getMacAddress():
    result = [True, None]
    def handleMessage(container, data):
        container[0] = False
        container[1] = data
    subscriptionId = BluenetEventBus.subscribe(DevTopics.ownMacAddress, lambda data: handleMessage(result, data))
    bluenet._usbDev.requestMacAddress()
    time.sleep(0.5)
    BluenetEventBus.unsubscribe(subscriptionId)
    return result[1]




