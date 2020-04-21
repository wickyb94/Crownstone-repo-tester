import RPi.GPIO as GPIO
import time


# these are the pins S0,S1,S2,S3,EN of the multiplexer connected to the Raspberry PI
mp = [6,13,19,26,21]

GPIO.setmode(GPIO.BCM)

for setting in range(0,5):
    GPIO.setup(mp[setting],GPIO.OUT)

#function where you can decide wich channel is connected. It ranges from 1
def multiplex(channel):
    channel = channel-1
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
    time.sleep(0.5)

#cleanup only needed in the main code
#GPIO.cleanup()
