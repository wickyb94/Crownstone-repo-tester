import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)

print "LED on"
GPIO.output(16,GPIO.HIGH)
time.sleep(1)
print "LED OFF"
GPIO.output(16,GPIO.LOW)
time.sleep(1)

