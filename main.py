from jlink import *
from relaisiopi import *
from multiplexer import *

bus.write_pin(1 , 0)
multi(5)
ob = Programmer()
commands = JLink(ob)
jlinktupp = commands.run_commands(['connect','i','exit'], 4)
jlinkout = jlinktupp.split('3.300V')[1]
print (jlinktupp)
bus.write_pin(1 , 1)

GPIO.cleanup()
