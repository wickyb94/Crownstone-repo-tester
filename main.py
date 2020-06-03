from jlink import *
from relaisiopi import *
from multiplexer import Multiplexer
from uarttest import *
import math

#The main script excecutes the tests and functions of the other scripts
# These are the pins S0,S1,S2,S3,EN of the multiplexer connected to the Raspberry PI
mp = [6, 13, 19, 26, 21]

GPIO.setmode(GPIO.BCM)
for setting in range(0, 5):
    GPIO.setup(mp[setting], GPIO.OUT)

bluenet.initializeUSB("/dev/ttyUSB0")

ob = Programmer()
commands = JLink(ob)
multiplexers = []
crownstoneCount = 3
crownstonePerMultiplexer = 16

multiplexer1 = Multiplexer (mp[0], mp[1], mp[2], mp[3], mp[4])
multiplexers.append(multiplexer1)

for select in range(1, crownstoneCount):
    setRelayOn(select)
    
    multiplexerId = math.floor(select / crownstonePerMultiplexer)
    multiplexers[multiplexerId].switch (select)

    jlinktupp = commands.run_filename('/home/pi/firmware-tester/loaddevfirmware.script', 20)
    jlinkout = jlinktupp.split('3.300V')[2]
    print(jlinkout)
    print('update is done ')
    time.sleep(1)

    print(getMacAddress())

    setRelayOff(select)


bluenet.stop()
GPIO.cleanup()
