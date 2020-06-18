import multiplexer

''''the class Multiplexers makes multiple multiplexers and combine them so there is only 1 function needed to control them''''      
class Multiplexers:
   # creating a list of multiple multiplexers and adding them to the list
    multiplexers = []
    multiplexer1 = Multiplexer (mp1[0], mp1[1], mp1[2], mp1[3], mp1[4])
    multiplexer2 = Multiplexer (mp2[0], mp2[1], mp2[2], mp2[3], mp2[4])
    multiplexers.append (multiplexer1)
    multiplexers.append (multiplexer2)
    
   ''''function where you can decide wich channel is connected. It ranges from 0 to 31''''
    def switchChannel(channel):
        #calculates wich multiplexer to choose from
        multiplexerId = math.floor (channel / numOffChannels)
        #checks if the channel is in range
        if multiplexerId < numOffMultiplexers:
            #calculates wich channels is used 
            channel = channel - numOffChannels * multiplexerId
            multiplexers[multiplexerId].switch (channel)
        else:
            raise Exception ('Channel number out of bounds, channel must be an integer from 0 to 31')
        
   ''''function to test all if all the channels of the multiplexers are still working''''             
    def testAllOutputs (self):
        for channel in range (0, numOffChannels * nummOffMultiplexers):
            self.switchChannel (channel)
            #sleep is needed here because only 1 channel can be choosen on the same time
            time.sleep (0.1)
            

    ''''gets the max number of channels available''''
    def getmaxNumChannels():
        return numOffChannels * numOffMultiplexers    
    
