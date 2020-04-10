import subprocess
import time
from jlink import *

#cjlink = ['/opt/JLink_Linux_V664_arm/JLinkExe', '-Device', 'NRF52832_XXAA', '-speed', '4000', '-if', 'SWD', '-autoconnect', '1']
#flash_command = cjlink + ['i']
#session = subprocess.Popen(cjlink, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#time.sleep(5)
#print(session.returncode)
#stdout = session.communicate()


if session.returncode != 0:
    print("FAILED!")

#print(session.returncode)


a=JLink('NRF52832_XXAA')
a.run_commands('i',60)