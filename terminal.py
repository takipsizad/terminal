import platform
import subprocess
import asyncio
import websockets
import random
import socket
import json
import time
import os
from pytube import YouTube
from pathlib import Path
import requests
import mojang
from tkinter import *
import webbrowser
import urllib.request
pip = 'pip install '
system = platform.platform()
release = platform.release()
version = platform.version()
print('design by takipsizad 2020  currently working on ' + system + version + ' source code: write sourcecode to open source code')

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
    print ('closing')
    time.sleep(0.1)
    print ('[===d|*|b===]')
    time.sleep(0.1)
    time.sleep(0.1)
    print('done')
    exit()

def exitcheck():
    if 'exit' == cmd:
        exits()

def textcheck():
    if 'text' == cmd:
        textc()

def pythonversion():
    print (platform.python_version())

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
    time.sleep(0.4)
    print ('fullosname')
    time.sleep(0.4)
    print ('exit')
    time.sleep(0.4)
    print ('system')
    time.sleep(0.4)
    print ('help')
    time.sleep(0.4)
    print ('text')
    time.sleep(0.4)
    print ('pythonver')
    time.sleep(0.4)
    print ('execute')
    time.sleep(0.4)
    print ('evalpy')
    time.sleep(0.4)
    print ('youtube')
    time.sleep(0.4)
    print ('ip')
    time.sleep(0.4)
    print ('pip install')
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
def win_edition():
    print(platform.win32_edition())

def helpcheck():
    if 'help' == cmd:
        help()

def win32_editioncheck():
    if 'winedition' == cmd:
        if 'Windows' == platform.system():
            win_edition()
        else:
            print("ERROR this isnt windows os")

def creditcheck():
    if 'credits' == cmd:
        creditst()

def creditst():
    print("credits:")
    time.sleep(0.5)
    print ("takipsizad 2020")
    
def evscheck():
    if 'evalpy' == cmd:
        evals()

def evals():
    print('write the thing that you want to execute as python code')
    evalcmd = input()
    print(eval(evalcmd))

def ipcheck():
    if 'ip' == cmd:
        ipprint()

def ipprint():
    os.system('ipconfig')

def youtubedownload():
    print ('write the link of youtube video that you want do download')
    ytlink = input()
    yt = YouTube(ytlink)
    stream = yt.streams.first()
    stream.download("videos")
    print ('done')

def musicdownload():
    print ('write the link of youtube video that you want do download')
    ytmusiclink = input()
    yt = YouTube(ytmusiclink)
    stream = yt.streams.filter(audio_only=True).first()
    stream.download("music")

def musicdownloadcheck():
    if 'youtube download music' == cmd:
        musicdownload()

def youtubedownloadcheck():
    if 'youtube download video' ==cmd:
        youtubedownload()

def youtubehelp():
    print("commands:")
    time.sleep(0.4)
    print("youtube download video")
    time.sleep(0.4)
    print("youtube download music")
    time.sleep(0.4)
    print('youtube video info')
    time.sleep(0.4)
    print('youtube video info save')
    print('              ')

def youtubehelpc():
    if 'youtube' == cmd:
        youtubehelp()

def pipinstall():
    print("write the name of package that you want to install")
    pythonpack = input()
    os.system(pip + pythonpack)

def pipinstallcheck():
    if 'pip install' == cmd:
        pipinstall()

def ytinfo():
    print ('write to link to video that you want to get information about ')
    ytinfolink = input()
    yt = YouTube(ytinfolink)
    print('infos:')
    time.sleep(0.4)
    print('title')
    print(yt.title)
    time.sleep(0.4)
    print('author')
    print(yt.author)
    time.sleep(0.4)
    print('description')
    print(yt.description)
    time.sleep(0.4)
    print('keywords') 
    print(yt.keywords)
    time.sleep(0.4)
    print('length in second')
    print(yt.length )
    time.sleep(0.4)
    print('metadata')
    print(yt.metadata)
    time.sleep(0.4)
    print('publish date')
    print(yt.publish_date)
    time.sleep(0.4)
    print('rating')
    print(yt.rating)
    time.sleep(0.4)
    print('views')
    print(yt.views)

def videocheck():
    if 'youtube video info' == cmd:
        ytinfo()

def youtubevideoinfosave():
    print ('write to link to video that you want to get information about ')
    texti = input()
    yt = YouTube(texti)
    info = open(yt.title + '.txt',"w+")
    info.write(yt.title + ' :title \n')
    info.write(yt.author + ' :author\n')
    info.write(yt.description + ' :description\n')
    info.write(yt.length + ' seconds :length\n')
    info.write(yt.publish_date + ' :publish_date\n')
    info.write(yt.rating + ' :rating\n')
    info.write(yt.views + ' :views\n')
    print ("done")

def youtubevideoinfosavecheck():
    if 'youtube video info save' == cmd:
        youtubevideoinfosave()

def haveibeenpwned():
    print("write your password")
    password = input()
    pwned = requests.get('https://api.leakedpassword.com/pass/' + password)
    print (pwned.json())

def haveibeenpwndedcheck():
    if 'haveibeenpwned' == cmd:
        haveibeenpwned()

def isiplegit():
    print ('write ip that you want to check')
    ip = input()
    ipcheck = requests.get('https://api.iplegit.com/full?ip=' + ip)
    print (ipcheck.json())

def isiplegitcheck():
    if 'ipcheck' == cmd:
        isiplegit()

def sourcecode():
    webbrowser.open("https://github.com/takipsizad/terminal")

def sourcecodecheck():
    if 'sourcecode' == cmd:
        sourcecode()

def qrcode():
    qrinfo = input()
    url = "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=" + qrinfo
    r = urllib.request.urlopen(url)
    with open("qr.png", "wb") as f:
        f.write(r.read())

def qrcodecheck():
    if 'qrcode' == cmd:
        qrcode()

while True:
    cmd = input()
    systemcheck()
    fullosnamecheck()
    exitcheck()
    textcheck()
    helpcheck()
    pythonversioncheck()
    executescheck()
    win32_editioncheck()
    creditcheck()
    evscheck()
    ipcheck()
    youtubedownloadcheck()
    musicdownloadcheck()
    youtubehelpc()
    pipinstallcheck()
    youtubevideoinfosavecheck()
    videocheck()
    haveibeenpwndedcheck()
    isiplegitcheck()
    sourcecodecheck()
    qrcodecheck()
