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


def relayErrors(errornumber):
    if errornumber == 1:
        print('input out of bound input must be an integer from 1 to 32')

def setRelayOn(relaynumber):
    if relaynumber > 0 and relaynumber < 17:
        bus1.write_pin(relaynumber, 0)
    elif relaynumber > 16 and relaynumber < 33:
        bus2.write_pin((relaynumber-16), 0)
    elif relaynumber < 0:
        relayErrors(1)
    elif relaynumber > 32:
        relayErrors(1)

def setRelayOff(relaynumber):
    if relaynumber > 0 and relaynumber < 17:
        bus1.write_pin(relaynumber, 1)
    elif relaynumber > 16 and relaynumber < 33:
        bus2.write_pin((relaynumber - 16), 1)
    elif relaynumber < 0:
        relayErrors(1)
    elif relaynumber > 32:
        relayErrors(1)

def setAllRelayOn():
    for relaynumber in range(17, 33):
        setRelayOn(relaynumber)
        time.sleep(0.5)

def setAllRelayOff():
    for relaynumber in range(17, 33):
        setRelayOff(relaynumber)
        time.sleep(0.5)

