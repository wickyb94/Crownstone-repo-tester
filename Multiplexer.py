import RPi.GPIO as GPIO
import time

S0 = 6
S1 = 13
S2 = 19
S3 = 26
sic = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(S0, GPIO.OUT)
GPIO.setup(S1, GPIO.OUT)
GPIO.setup(S2, GPIO.OUT)
GPIO.setup(S3, GPIO.OUT)
GPIO.setup(sic, GPIO.OUT)

def multi(channel):
    controlPin = [S0, S1, S2, S3] 
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
    
    for i in range(0,4):
        GPIO.output(controlPin[i],muxChannel[channel][i])

GPIO.output(sic,GPIO.HIGH)



multi(2)
print( "test 1")
time. sleep(3)
multi(14)
time.sleep(3)
print ("test 2")




GPIO.cleanup()
