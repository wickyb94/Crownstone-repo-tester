from IOPi import IOPi
import time

#setting up the busses of the IO-extenssion board to control the relay module
relay1 = IOPi(0x21)
relay1.set_port_direction(0, 0x00)
relay1.set_port_direction(1, 0x00)
relay1.write_port(0, 0xFF)
relay1.write_port(1, 0xFF)

#a function that controls the relay choose the board relay1 or relay 2
# relaynumber is wich relay on that board you want to swicht and relaystate is true or false
def setrelay(relayboard,relaynumber,relaystate):
    if relayboard == relay1 and relaystate == True:
        relayboard.write_pin(relaynumber,0)
    elif relayboard == relay1 and relaystate == False:
        relayboard.write_pin(relaynumber,1)


