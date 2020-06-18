from jlink import *
from relayboards import *
from multiplexers import *
from uarttest import *
import math
import email

''''The main script excecutes the tests and functions of the other scripts''''

fh = open('demo.txt', 'w')

sender_email = 'wicky_bhaggoe@hotmail.com'
rec_email = 'wicky_bhaggoe@hotmail.com'
password = 'Slaapkamer1!'
subject = 'pycharm'
body = 'Hi i am a mail from python'
filename = 'demo.txt'

#Intitializing the usb port wich will be used for the bluenet library 
bluenet.initializeUSB ("/dev/ttyUSB0")

# setting up how many crownstones are used and initializing the classes wich are needed
crownstoneCount = 2
ob = Programmer ()
commands = JLink (ob)
crownstonePerMultiplexer = 16

multiplexers = Multiplexers()
relayboards = Relayboards()

for select in range (0, crownstoneCount):
    relayboards.setRelayOn (select)
    
    multiplexers.switchChannel(select)

    jlinkTupp = commands.run_filename ('/home/pi/firmware-tester/loaddevfirmware.script', 20)
    jlinkOut = jlinkTupp.split ('3.300V')[2]
    succesCount = jlinkTupp.count ('J-Link: Flash download')
    if succesCount == 3:
        print ('update is done')
    else:
        raise Exception ('update failed')

    print (getMacAddress())

    relayboards.setRelayOff (select)


bluenet.stop ()
GPIO.cleanup ()
