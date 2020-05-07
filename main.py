from jlink import *
from relaisiopi import *
from multiplexer import *
from uarttest import *
import asyncio, time
from setuart import *
#test = 1


#multiplex(1)

#print(findUsbBleDongleHciIndex())
#enableUart('HelloWorld')
uart('HelloWorld')



#using a function from jlink.py to run a few command when doing that the first command must be connect
'''
ob = Programmer()
commands = JLink(ob)
jlinktupp = commands.run_commands(['connect','i','mem32 0 10','exit'], 4)
jlinkout = jlinktupp.split('3.300V')[1]
print (jlinkout)
'''
'''
ob = Programmer()
commands = JLink(ob)
jlinktupp = commands.run_filename('/home/pi/firmware-tester/loadfirmware.script', 20)
jlinkout = jlinktupp.split('3.300V')[2]
print (jlinkout)
'''

print('test')
#uart('HelloWorld')
#test = input()


time.sleep(1)

GPIO.cleanup()
