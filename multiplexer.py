import RPi.GPIO as GPIO
import time

# Initializing the pins of the multiplexer these pins are S0,S1,S2,S3,EN of the multiplexer
mp1 = [6, 13, 19, 26, 21]
mp2 = [4, 17, 27, 22, 18]
GPIO.setmode (GPIO.BCM)

for setting in range (0, 5):
    GPIO.setup (mp1[setting], GPIO.OUT)
for setting in range (0, 5):
    GPIO.setup (mp2[setting], GPIO.OUT)
      
class Multiplexers():
   multiplexers = []
   multiplexer1 = Multiplexer (mp1[0], mp1[1], mp1[2], mp1[3], mp1[4])
   multiplexer2 = Multiplexer (mp2[0], mp2[1], mp2[2], mp2[3], mp2[4])
   multiplexers.append (multiplexer1)
   multiplexers.append (multiplexer2)
   
   def switchChannel(channel):
      multiplexerId = math.floor (channel / 16)
      if 0 =< channel =< 31:
         if multiplexerId == 0:
            multiplexers[multiplexerId].switch (channel)
         elif multiplexerId == 1:
            channel = channel - 16
            multiplexers[multiplexerId].switch (channel)
          else:
               raise Exception ('Channel number out of bounds, channel must be an integer from 0 to 31')
   def testAllOutputs (self):
      for channel in range (0, 32):
               self.switchChannel (channel)
               print (channel)
               time.sleep (0.1)
         
   # The multiplexer allows to switch between the different channels of the multiplexer 
   class Multiplexer (S0, S1, S2, S3, EN):
      # List of the 16 channels 
       muxChannel = [
                   [0, 0, 0, 0],
                   [1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [1, 1, 0, 0],
                   [0, 0, 1, 0],
                   [1, 0, 1, 0],
                   [0, 1, 1, 0],
                   [1, 1, 1, 0],
                   [0, 0, 0, 1],
                   [1, 0, 0, 1],
                   [0, 1, 0, 1],
                   [1, 1, 0, 1],
                   [0, 0, 1, 1],
                   [1, 0, 1, 1],
                   [0, 1, 1, 1],
                   [1, 1, 1, 1],
               ]

       def __init__ (self, S0, S1, S2, S3, EN):
           self.S0 = S0
           self.S1 = S1
           self.S2 = S2
           self.S3 = S3
           self.EN = EN

       #function where you can decide wich channel is connected. It ranges from 0 to 15
       def switch (self, channel):
           channel = channel-1
           if 0 =< channel =< 15:
               controlPin = [self.S0, self.S1, self.S2, self.S3]
               GPIO.output (self.EN, 1)
               for i in range (0, 4):
                   GPIO.output (controlPin[i], muxChannel[channel][i])
               GPIO.output(self.EN, 0)
           else:
               raise Exception ('Channel number out of bounds, channel must be an integer from 0 to 15')

       #function to test all if all the channels of this multiplexer are still working
       def testMultiplexerOutputs (self):
           for channel in range (0, 16):
               self.switch (channel)
               print (channel)
               time.sleep (0.1)

