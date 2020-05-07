import RPi.GPIO as GPIO
import time


# these are the pins S0,S1,S2,S3,EN of the multiplexer connected to the Raspberry PI
mp = [6, 13, 19, 26, 21]

GPIO.setmode(GPIO.BCM)
for setting in range(0, 5):
    GPIO.setup(mp[setting], GPIO.OUT)

def multiplexerErrors(errornumber):
    if errornumber == 1:
        print('input out of bound input must be an integer from 1 to 16')

#function where you can decide wich channel is connected. It ranges from 1 to 16
def multiplex(channel, S0, S1, S2, S3, EN):
    channel = channel-1
    if channel > 0 and channel < 17:
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


#cleanup only needed in the main code
#GPIO.cleanup()
