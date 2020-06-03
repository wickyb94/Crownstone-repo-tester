from IOPi import IOPi
import time

#setting up the busses of the IO-extenssion board to control the relay module
bus1 = IOPi(0x20)
bus1.set_port_direction(0, 0x00)
bus1.set_port_direction(1, 0x00)
bus1.write_port(0, 0xFF)
bus1.write_port(1, 0xFF)

bus2 = IOPi(0x21)
bus2.set_port_direction(0, 0x00)
bus2.set_port_direction(1, 0x00)
bus2.write_port(0, 0xFF)
bus2.write_port(1, 0xFF)

#Function where the user can turn on the choosen relay there are 32 to choose from.
def setRelayOn(relaynumber):
    if relaynumber > 0 and relaynumber < 17:
        bus1.write_pin(relaynumber, 0)
    elif relaynumber > 16 and relaynumber < 33:
        bus2.write_pin((relaynumber-16), 0)
    else:
        raise Exception ('relaynumber out of bounds, relaynumber must be an integer from 1 to 32')

#Function where the user can turn off the choosen relay there are 32 to choose from.
def setRelayOff(relaynumber):
    if relaynumber > 0 and relaynumber < 17:
        bus1.write_pin(relaynumber, 1)
    elif relaynumber > 16 and relaynumber < 33:
        bus2.write_pin((relaynumber - 16), 1)
    else:
        raise Exception ('relaynumber out of bounds, relaynumber must be an integer from 1 to 32')
        
#Function that alows the user to turn on all the relays. For safety reason the relays wont turn simultaneously. 
#The function is used to test if the relayboard works
def setAllRelayOn():
    for relaynumber in range(0, 33):
        setRelayOn(relaynumber)
        time.sleep(0.5)
        
#Function that alows the user to turn off all the relays. 
#The function is used to test if the relayboard works
def setAllRelayOff():
    for relaynumber in range(0, 33):
        setRelayOff(relaynumber)
