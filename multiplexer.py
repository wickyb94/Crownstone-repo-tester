import RPi.GPIO as GPIO
import time

class Multiplexer:
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

    #function where you can decide wich channel is connected. It ranges from 1 to 16
    def switch (self, channel):
        channel = channel-1
        if channel > -1 and channel < 17:
            controlPin = [self.S0, self.S1, self.S2, self.S3]

            GPIO.output(self.EN, 1)
            for i in range(0, 4):
                GPIO.output(controlPin[i], muxChannel[channel][i])
            GPIO.output(self.EN, 0)
        else:
            raise Exception ('Channel number out of bounds, channel must be an integer from 1 to 16")

    def testAllOutputs(self):
        for channel in range(1, 16):
            self.switch(channel)
            print(channel)
            time.sleep(0.1)

