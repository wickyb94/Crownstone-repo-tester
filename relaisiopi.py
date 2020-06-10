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

''''the class Multiplexers creates multiple relayboards and combine them so its easier to control them'''' 
class Relayboards:
    # creating a list of multiple relayboards and adding them to the list
    relayboards = []
    relayboard1 = Relayboard (bus1)
    relayboard2 = Relayboard (bus2)
    relayboards.append (relayboard1)
    relayboards.append (relayboard2)
    
    ''''Function where the user can turn on the choosen relay there are 32 to choose from but goes from 0-31.''''
    def setRelayOn (relaynumber):
        relayId = math.floor (relaynumber / numOffRelays)
        if 0 =< relaynumber =< numOffRelays * numOffBoards -1:
            if relayId == 0:
                relaynumber = relaynumber + 1
                relayboards[relayId].sellectRelayOn (relaynumber)
            elif multiplexerId == 1:
                relaynumber = relaynumber - (numOffRelays - 1)
                relayboards[relayId].sellectRelayOn (relaynumber)
            else:
                raise Exception ('relaynumber out of bounds, relaynumber must be an integer from 0 to 31')  
                
    ''''Function where the user can turn off the choosen relay there are 32 to choose from but goes from 0-31.''''
    def setRelayOff (relaynumber):
            relayId = math.floor (relaynumber / numOffRelays)
            if 0 =< relaynumber =< numOffRelays * numOffBoards -1:
                if relayId == 0:
                    relaynumber = relaynumber + 1
                    relayboards[relayId].sellectRelayOff (relaynumber)
                elif multiplexerId == 1:
                    relaynumber = relaynumber - (numOffRelays - 1)
                    relayboards[relayId].sellectRelayOff (relaynumber)
                else:
                    raise Exception ('relaynumber out of bounds, relaynumber must be an integer from 0 to 31')
  
    ''''Function that allows the user to turn on all the relays. 
    For safety reason the relays wont turn simultaneously. 
    The function is used to test if the relayboards works''''
    def setAllRelayOn():
        for relaynumber in range(0, 33):
            setRelayOn(relaynumber)
            time.sleep(0.5)

    ''''Function that allows the user to turn off all the relays. 
    The function is used to test if the relayboards works''''
    def setAllRelayOff():
        for relaynumber in range(0, 33):
            setRelayOff(relaynumber) 
            
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



        

