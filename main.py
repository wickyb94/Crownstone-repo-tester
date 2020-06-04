from jlink import *
from relaisiopi import *
from multiplexer import Multiplexer
from uarttest import *
import math

# The main script excecutes the tests and functions of the other scripts
# Initializing the pins of the multiplexer these pins are S0,S1,S2,S3,EN of the multiplexer
mp = [6, 13, 19, 26, 21]
GPIO.setmode (GPIO.BCM)
for setting in range (0, 5):
    GPIO.setup (mp[setting], GPIO.OUT)

# Intitializing the usb port wich will be used for the bluenet library 
bluenet.initializeUSB ("/dev/ttyUSB0")

# setting up how many crownstones are used and weet niet hoe ik de rest moet uitleggen 
crownstoneCount = 2
ob = Programmer ()
commands = JLink (ob)
crownstonePerMultiplexer = 16
multiplexers = []
multiplexer1 = Multiplexer (mp[0], mp[1], mp[2], mp[3], mp[4])
multiplexers.append (multiplexer1)

for select in range (1, crownstoneCount+1):
    setRelayOn (select)
    
    multiplexerId = math.floor (select / crownstonePerMultiplexer)
    multiplexers[multiplexerId].switch (select)

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
