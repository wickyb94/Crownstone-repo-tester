import subprocess
import time
from jlink import *

#code die hier staat niet meer nodig omdat er nu gebruik word gemaakt van jlink.py toch maar even bewaard

'''
cjlink = ['/opt/JLink_Linux_V664_arm/JLinkExe', '-Device', 'NRF52832_XXAA', '-speed', '4000', '-if', 'SWD', '-autoconnect', '1']
flash_command = cjlink + ['i']
session = subprocess.Popen(cjlink, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout = session.communicate()

for line in iter(stdout):
    if line.decode('utf-8') == '':
        break
    print(line.decode('utf-8'))

if session.returncode != 0:
    print("FAILED!")

print(session.returncode)

'''
ob = Programmer()
commands = JLink(ob)

jlinktupp = commands.run_commands(['connect','i','exit'], 4)
jlinkout = jlinktupp.split('3.300V')[1]
print (jlinktupp)

