import subprocess
from subprocess import Popen, PIPE

c = 'JLinkExe'
session = subprocess.Popen([c, '-ExitonError', '1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

hallo = session.stdout.decode("utf-8")

print("FAILED TO PROGRAM", hallo)

session.returncode