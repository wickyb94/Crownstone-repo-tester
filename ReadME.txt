FIRMWARE TESTER

Code that controlls and communicate with the Crownstones. The code is made for python3.
The main python code runs the other codes. 

Multiplexer: 
Setting up the pins on the Raspberry pi wich are used to switch between the channels on the Multiplexers

Relaisiopi:
Setting up the 2 busses on the Raspberry to contoll the 2 relay modules.

jlink,errors,base:
codes fom Adafruit used to communicate with the device connected on the jlink. 
for more info of the code go to the following site
https://github.com/adafruit/Adafruit_Adalink/blob/master/adalink/programmers/jlink.py
JlinkExe is needed on your device and can be found on the site of segger
https://www.segger.com/downloads/jlink

uarttest:
communicating to the devices with UART using the bluenet library.
for more information on the bluenet libary and how to install click the following link.
https://github.com/crownstone/bluenet/blob/master/README.md