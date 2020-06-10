from jlink import *
from relaisiopi import *
from multiplexer import Multiplexer
from uarttest import *
import math

# The main script excecutes the tests and functions of the other scripts

# Intitializing the usb port wich will be used for the bluenet library 
bluenet.initializeUSB ("/dev/ttyUSB0")

# setting up how many crownstones are used and weet niet hoe ik de rest moet uitleggen 
crownstoneCount = 2
ob = Programmer ()
commands = JLink (ob)
crownstonePerMultiplexer = 16

multiplexers = Multiplexers()

for select in range (0, crownstoneCount):
    setRelayOn (select)
    
    multiplexers.switchChannel(select)

    jlinkTupp = commands.run_filename ('/home/pi/firmware-tester/loaddevfirmware.script', 20)
    jlinkOut = jlinkTupp.split ('3.300V')[2]
    succesCount = jlinkTupp.count ('J-Link: Flash download')
    if succesCount == 3:
        print ('update is done')
    else:
        raise Exception ('update failed')

    print (getMacAddress())

    setRelayOff (select)


bluenet.stop ()
GPIO.cleanup ()
