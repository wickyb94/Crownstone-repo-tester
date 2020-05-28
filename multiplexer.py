import RPi.GPIO as GPIO
import time

def multiplexerErrors(errornumber):
    if errornumber == 1:
        print('input out of bound input must be an integer from 1 to 16')

#function where you can decide wich channel is connected. It ranges from 1 to 16
def multiplex(channel, S0, S1, S2, S3, EN):
    channel = channel-1
    if channel > -1 and channel < 17:
        controlPin = [S0, S1, S2, S3]
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
        GPIO.output(EN, 1)
        for i in range(0, 4):
            GPIO.output(controlPin[i], muxChannel[channel][i])
        GPIO.output(EN, 0)
        time.sleep(0.5)
    else:
        multiplexerErrors(1)

def testalloutputs(S0, S1, S2, S3, EN):
    for channelnumber in range(1, 16):
        multiplex(channelnumber, S0, S1, S2, S3, EN)
        print(channelnumber)
        time.sleep(0.1)

