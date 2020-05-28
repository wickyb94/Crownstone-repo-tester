from BluenetLib import Bluenet, BluenetEventBus, UsbTopics, Util
from LogUtil import *
import time

bluenet2 = Bluenet()
# enable UART
def enableUart(HelloWorld):
    bluenet2.initializeUSB("/dev/ttyUSB0")
    time.sleep(1)
    print(gt(), "----- Enabling UART...")
    bluenet2._usbDev.setUartMode(3)
#    print('1')
#    bluenet2.initializeUSB("/dev/ttyUSB0")
#    bluenet2.stop()

'''
bluenet.initializeUSB("/dev/ttyUSB0")
print('test')
bluenet.bluenetBLE = BluenetBle(hciIndex=1)
print('test2')
bluenet.bluenetBLE.setSettings(
	adminKey="adminKeyForCrown",
	memberKey="memberKeyForHome",
	basicKey="guestKeyForOther",
	serviceDataKey="guestKeyForOther",
	localizationKey="localizationKeyX",
	meshApplicationKey="meshKeyForStones",
	meshNetworkKey="meshAppForStones",
)
print('tt')
bluenet.stop()
'''
result = [True, None]
def handleMessage(container, data):
    container[0] = False
    container[1] = data

'''
subscriptionId = BluenetEventBus.subscribe(DevTopics.ownMacAddress, lambda data: handleMessage(result, data))
bluenet._usbDev.requestMacAddress()
BluenetEventBus.unsubscribe(subscriptionId)
counter = 0
while result[0] and counter < 50:
    counter += 1
    time.sleep(0.5)
print(result[1])
bluenet.stop()
'''
