import platform
import subprocess
import sys
import asyncio
import websockets
import random
import socket
import time
import json
import time
import os


system = platform.platform()
release = platform.release()
version = platform.version()

def systemcheck():
    if 'system' == cmd:
        system()

def system():
    print (platform.machine())
    print (platform.platform())

def fullosnamecheck():
    if 'fullosname' == cmd:
         fullosname()

def fullosname():
     print (platform.uname())

def exits():
    exit()

def exitcheck():
    if 'exit' == cmd:
        exits()

def textcheck():
    if 'text' == cmd:
        textc()

def pythonversion():
    print (platform.python_version())

def javaver():
    print (platform.java_ver())

def javavercheck():
    if 'javaver' == cmd:
        javaver()

def textc():
    print ('write text that you want as file name')
    texti = input()
    my_file = open(texti,"w+")
    print ("write the thing that you want to write")
    texts = input()
    my_file = open(texti,"w+")
    my_file.write(texts)
    print ("done")

def help():
    print ('commands:')
    time.sleep(1)
    print ('fullosname')
    time.sleep(1)
    print ('exit')
    time.sleep(1)
    print ('system')
    time.sleep(1)
    print ('help')
    time.sleep(1)
    print ('text')
    time.sleep(1)
    print ('pythonver')
    time.sleep(1)
    print ('javaver')
    print ('   ')

def executes():
    print ("input the command that you want to execute")
    command = input()
    os.system(command)
    print ('command executed')

def executescheck():
    if 'execute' == cmd:
        executes()
def pythonversioncheck():
    if 'pythonver' == cmd:
        pythonversion()

def helpcheck():
    if 'help' == cmd:
        help()

while True:
    cmd = input()
    systemcheck()
    fullosnamecheck()
    exitcheck()
    textcheck()
    helpcheck()
    pythonversioncheck()
    javavercheck()
    executescheck()