import relayboard

''''the class relayboards creates multiple relayboards and combine them so its easier to control them'''' 
class Relayboards:
    # creating a list of multiple relayboards and adding them to the list
    relayboards = []
    relayboard1 = Relayboard (bus1)
    relayboard2 = Relayboard (bus2)
    relayboards.append (relayboard1)
    relayboards.append (relayboard2)
    
    ''''Function where the user can turn on the choosen relay there are 32 to choose from but goes from 0-31.''''
    def setRelayOn (relaynumber):
        #Calculates wich baord to choose from
        relayId = math.floor (relaynumber / numOffRelays)
        #checks if the relaynumber that is given is in range
        if relayId < numOffBoards:
            #calculates wich relay is given on the choosen board
            relaynumber = relaynumber * relayId + 1
            relayboards[relayId].sellectRelayOn (relaynumber)
        else:
            raise Exception ('relaynumber out of bounds, relaynumber must be an integer from 0 to 31')  
                
    ''''Function where the user can turn off the choosen relay there are 32 to choose from but goes from 0-31.''''
    def setRelayOff (relaynumber):
        #Calculates wich baord to choose from
        relayId = math.floor (relaynumber / numOffRelays)
        #checks if the relaynumber that is given is in range
        if relayId < numOffBoards:
            #calculates wich relay is given on the choosen board
            relaynumber = relaynumber * relayId + 1
            relayboards[relayId].sellectRelayOff (relaynumber)
        else:
            raise Exception ('relaynumber out of bounds, relaynumber must be an integer from 0 to 31')
  
    ''''Function that allows the user to turn on all the relays. 
    For safety reason the relays wont turn simultaneously. 
    The function is used to test if the relayboards works''''
    def setAllRelayOn():
        for relaynumber in range(0, numOffRelays * numOffBoards + 1):
            setRelayOn(relaynumber)
            time.sleep(0.5)

    ''''Function that allows the user to turn off all the relays. 
    The function is used to test if the relayboards works''''
    def setAllRelayOff():
        for relaynumber in range(0, numOffRelays * numOffBoards + 1):
            setRelayOff(relaynumber) 
            
 
