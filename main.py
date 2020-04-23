from jlink import *
from relaisiopi import *
from multiplexer import *
from uarttest import *
#test = 1

setrelay(relay1,1,True)
multiplex(1)
'''
#using a function from jlink.py to run a few command when doing that the first command must be connect
ob = Programmer()
commands = JLink(ob)
jlinktupp = commands.run_commands(['connect','i','mem32 0 10','exit'], 4)
jlinkout = jlinktupp.split('3.300V')[1]
print (jlinkout)
'''
uart('HelloWorld')
#test = input()

setrelay(relay1,1,False)
time.sleep(1)

GPIO.cleanup()
