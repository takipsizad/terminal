import platform
import subprocess
import sys
system = platform.platform()
release = platform.release()
version = platform.version()

def systemcheck():
    if 'system' == cmd:
        system()
def system():
    print (platform.machine())
    print (platform.platform())




def fullosname():
     print (platform.uname())

while True:
     cmd = input()
    