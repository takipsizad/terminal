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
        text()

def text():
    print ('write the text that you want')
    texti = input()
    print ('write the name of the file')
    textn = input()
    my_file = open(textn,"w+")
    my_file = open("this_is_file.txt","w+")
    my_file.write("Hey This text is going to be added to the text file yipeee!!!")

    

while True:
    cmd = input()
    systemcheck()
    fullosnamecheck()
    exitcheck()
    textcheck()