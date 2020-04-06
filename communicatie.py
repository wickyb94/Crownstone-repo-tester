import subprocess
from subprocess import *

c = ['lxterminal','-e','/home/pi/bestanden/JLink_Linux_V664_arm/JLinkExe']
session = subprocess.Popen(c, stdin=PIPE, stdout=PIPE, stderr=PIPE)





print('test')
#s1.communicate('i')

#-Device NRF52832_XXAA -speed 400 -if SWD -autoconnect 1
#s1 = subprocess.Popen('i' ,shell = True)

