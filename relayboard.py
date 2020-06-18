from IOPi import IOPi
import time
import math

''''setting up the busses of the IO-extenssion board to control the relay module board''''
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

#with these variables you can decide how many boards there are and how many Relays there are on each board
numOffRelays = 16
numOffBoards = 2

'''''with this class a relayboard can be made to choose the relay''''
class Relayboard:
    def __init__ (self, bus):
        self.bus = bus

    ''''Function where the user can turn on the choosen relay there are 16 to choose frombut goes from 0-15.''''
    def sellectRelayOn(self, relaynumber):
        if 0 >= relaynumber =< 15:
            relaynumber = relaynumber + 1
            self.bus.write_pin(relaynumber, 0)
        else:
            raise Exception ('relaynumber out of bounds, relaynumber must be an integer from 0 to 15')

    ''''Function where the user can turn off the choosen relay there are 16 to choose from but goes from 0-15.''''
    def sellectRelayOff(self, relaynumber):
        if 0 >= relaynumber =< 15:
            relaynumber = relaynumber + 1
            self.bus.write_pin(relaynumber, 1)
        else:
            raise Exception ('relaynumber out of bounds, relaynumber must be an integer from 0 to 15')
