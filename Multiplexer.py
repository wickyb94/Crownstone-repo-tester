import RPi.GPIO as GPIO
import time
import subprocess
# dit zijn de pinnen S0,S1,S2,S3,EN op de multiplexer 
mp = [6,13,19,26,20]  

GPIO.setmode(GPIO.BCM)

for setting in range(0,5):
    GPIO.setup(mp[setting],GPIO.OUT)
def formule (self,y,x):
    self.c = y + x
    return self.c
def multi(channel):
    controlPin = [mp[0],mp[1],mp[2],mp[3]] 
    muxChannel = [
        [0,0,0,0],
        [1,0,0,0],
        [0,1,0,0],
        [1,1,0,0],
        [0,0,1,0],
        [1,0,1,0],
        [0,1,1,0],
        [1,1,1,0],
        [0,0,0,1],
        [1,0,0,1],
        [0,1,0,1],
        [1,1,0,1],
        [0,0,1,1],
        [1,0,1,1],
        [0,1,1,1],
        [1,1,1,1],
    ]
    GPIO.output(mp[4],1)
    for i in range(0,4):
        GPIO.output(controlPin[i],muxChannel[channel][i])
    GPIO.output(mp[4],0)

inp = 1
print('hallo')
#while inp == 1:
#    multi(0)
#    print(inp)
#    inp = input()
#print(inp)
#for x in range(0,16):
#    multi(x)
#    print(x)
#    time. sleep(0.5)
#multi(1)

GPIO.cleanup()
