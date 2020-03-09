import RPi.GPIO as GPIO
import time

// bla
een  = 6
twee = 13
drie = 19
vier = 26
vijf = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(een, GPIO.OUT)
GPIO.setup(twee, GPIO.OUT)
GPIO.setup(drie, GPIO.OUT)
GPIO.setup(vier, GPIO.OUT)
GPIO.setup(vijf, GPIO.OUT)

GPIO.output(een,GPIO.HIGH)
GPIO.output(twee,GPIO.HIGH)
GPIO.output(drie,GPIO.HIGH)
GPIO.output(vier,GPIO.HIGH)

GPIO.output(een,GPIO.LOW)
print( "test 1")
time.sleep(3)
GPIO.output(twee,GPIO.LOW)
print( "test 1")
time.sleep(3)
GPIO.output(drie,GPIO.LOW)
print( "test 1")
time.sleep(3)
GPIO.output(vier,GPIO.LOW)
print( "test 1")
time.sleep(3)






GPIO.cleanup()
