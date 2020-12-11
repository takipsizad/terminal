import platform
system = platform.platform()
release = platform.release()
version = platform.version()

def system():
    print (platform.machine())
    print (platform.platform())

cmd = input()
if 'system' == cmd:
    system()