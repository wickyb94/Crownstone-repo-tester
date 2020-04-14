from jlink import *
from relaisiopi import *
from multiplexer import *
a = 1
while a == 1:
    bus.write_pin(1,0)
    multi(1)
    time.sleep(0.5)

    ob = Programmer()
    commands = JLink(ob)
    jlinktupp = commands.run_commands(['connect','i','mem32 0 10','exit'], 4)
    jlinkout = jlinktupp.split('3.300V')[1]
    print (jlinkout)
    a = input()
bus.write_pin(1 , 1)
time.sleep(1)



GPIO.cleanup()
