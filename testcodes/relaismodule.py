import RPi.GPIO as GPIO
import time
#test om te kijken of de relaismodule werkte zonder de io-expander
rel = [6, 13, 19, 26] 

GPIO.setmode(GPIO.BCM)
for seting in range(0,4):
    GPIO.setup(rel[seting],GPIO.OUT)

for x in range(0,4):
    GPIO.output(rel[x],GPIO.HIGH)

for y in range(0,4):
    GPIO.output(rel[y],GPIO.LOW)
    print( "test")
    time.sleep(3)


GPIO.cleanup()
