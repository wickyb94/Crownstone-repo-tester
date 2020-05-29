from jlink import *
from relaisiopi import *
from multiplexer import *
from uarttest import *

bluenet.initializeUSB("/dev/ttyUSB0")

ob = Programmer()
commands = JLink(ob)
jlinktupp = commands.run_filename('/home/pi/firmware-tester/loadfactoryfirmware.script', 20)
jlinkout = jlinktupp.split('3.300V')[2]
print(jlinkout)
print('update is done ')
time.sleep(1)

bluenet._usbDev.setUartMode(3)
time.sleep(1)

print(getMacAddress())

bluenet.stop()
