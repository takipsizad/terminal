import random
import socket
import json
import time
import os
import pytube
from pytube import YouTube
from pathlib import Path
import requests
import mojang
from tkinter import *
import tkinter
import webbrowser
import urllib.request
import urllib.request
import shutil
import tarfile
from pypresence import Presence
import time
import configparser
config = configparser.ConfigParser()
config.read('settings.ini')
settings = config['settings']
serveradress = settings['serveradress']
discordrpc = settings['discordrpc']
client_id = ''  
RPC = Presence(client_id)
pip = 'pip install '
system = platform.platform()
release = platform.release()
version = platform.version()
print('design by takipsizad 2020  currently working on ' + system + version + '\n source code: write sourcecode to open github page')
if ('true' == discordrpc):
    RPC.connect()
    RPC.update(state="Running terminal", details="Running terminal",large_image="icon", large_text="made by takipsizad",small_image="icon2", small_text="Have a good day!",start=int(time.time()))
    

def systemcheck():
    if 'system' == cmd:
        systeme()

def systeme():
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
    time.sleep(0.2)
    print ('fullosname')
    time.sleep(0.2)
    print('credits')
    time.sleep(0.2)
    print ('exit')
    time.sleep(0.2)
    print ('system')
    time.sleep(0.2)
    print ('help')
    time.sleep(0.2)
    print ('text')
    time.sleep(0.2)
    print ('pythonver')
    time.sleep(0.2)
    print ('execute')
    time.sleep(0.2)
    print ('evalpy')
    time.sleep(0.2)
    print ('youtube')
    time.sleep(0.2)
    print ('ip')
    time.sleep(0.2)
    print ('pip install')
    time.sleep(0.2)
    print ('haveibeenpwndedcheck')
    time.sleep(0.2)
    print('ipcheck')
    time.sleep(0.2)
    print('qrcode')
    time.sleep(0.2)
    print('langdetect')
    time.sleep(0.2)
    print('winedition')
    time.sleep(0.2)
    print('haveibeenpwned')
    time.sleep(0.2)
    print('shadoweval')
    time.sleep(0.2)
    print('ip')
    time.sleep(0.2)
    print('webblacklist')
    time.sleep(0.2)
    print('discordrpc')
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
    stream = yt.streams.filter(only_audio=True).first()
    stream.download("music")
    print('done')

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
    jsonr = json.dumps(pwned.json())
    print('is it leaked')
    parsed_json = json.loads(jsonr)
    parsed_json2 = parsed_json['password']
    print(parsed_json2['leak'])
    print('if its how many times:')
    print(parsed_json2['seen'])



def haveibeenpwndedcheck():
    if 'haveibeenpwned' == cmd:
        haveibeenpwned()

def isiplegit():
    print ('write ip that you want to check')
    ip = input()
    ipcheck = requests.get('https://api.iplegit.com/info?ip=' + ip)
    jsonr = json.dumps(ipcheck.json())
    parsed_json = json.loads(jsonr)
    parsed_json2 = parsed_json['bad']
    parsed_json3 = parsed_json['type']
    parsed_json4 = parsed_json['ip']
    print('checked ip adress')
    print(parsed_json4)
    print('type')
    print(parsed_json3)
    print('bad:')
    print (parsed_json2)

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

def langdetect():
    print('write the text that you want to detect language from that')
    text = input()
    res = requests.get('http://' + serveradress + '/api/langdetect?text=' + text)
    jsonr = json.dumps(res.json())
    parsed_json = json.loads(jsonr)
    parsed_json2 = parsed_json['lang']
    print(parsed_json2)

def langdetectcheck():
    if 'langdetect' == cmd:
        langdetect()

def blacklistwgz():
    tar = tarfile.open(name='blackweb.tar.gz', mode='r:gz')
    tar.extractall()

def blacklistwopen():
    print('write the link to web adress')
    sitel = input()
    with open('blackweb.txt') as f:
        if sitel in f.read():
            print("found " + sitel + ' in list go at your own risk')
        else: 
            print ('not found')

def blacklistwhelpc():
    if 'webblacklist' == cmd:
        blacklistwhelp()

def blacklistwopenc():
    if 'webblacklist search' == cmd:
        blacklistwopen()

def blacklistwdownloader():
    url = "https://github.com/takipsizad/webblacklist/raw/main/blackweb.tar.gz"
    r = urllib.request.urlopen(url)
    with open("blackweb.tar.gz", "wb") as f:
        f.write(r.read())
    print('done!')

def blacklistwhelp():
    print('commands:')
    print('webblacklist search')
    print('webblacklist download')

def webblacklistdownloaderc():
    if 'webblacklist download' == cmd:
        blacklistwdownloader()
        print('download done!')
        blacklistwgz()
def shadoweval():
    print('shadow eval')
    shadowcmd = input()
    eval(shadowcmd)

def shadowevalc():
    if 'shadoweval' == cmd:
        shadoweval()

def discordrpco():
    RPC.connect()
    RPC.update(state="Running terminal", details="Running terminal",large_image="icon", large_text="made by takipsizad",small_image="icon2", small_text="Have a good day!",start=int(time.time()))
    print('started discordrpc')
def discordrpcoc():
    if 'discordrpc' == cmd:
        discordrpco()

def textread():
    print('enter file name without .txt ')
    filename = input()
    ObjRead = open(filename + ".txt", "r")
    txtContent = ObjRead.read()
    root = Tk()
    root.geometry('350x80')
    root.configure(background='#F0F8FF')
    root.title('Terminal text widget')
    Label(root, text=txtContent, bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=1, y=10)
    RPC.update(state="Running terminal text widget", details=txtContent,large_image="icon", large_text="made by takipsizad",small_image="icon2", small_text="Have a good day!" )
    ObjRead.close()
    time.sleep(15)

def textwidget():
    if 'textwidget' == cmd:
        textread()

def serverversion():
    res = requests.get('http://' + serveradress + '/api/serverversion')
    jsonr = json.dumps(res.json())
    parsed_json = json.loads(jsonr)
    parsed_json2 = parsed_json['serverversion']
    print(parsed_json2)

def serverversionc():
    if 'serverversion' == cmd:
        serverversion()

def settingse():
    print('write the setting you want to modify options:')
    for key in config['settings']:  
        print(key)
    setting = input()
    print(settings[setting])
    print("write the value that you want to change")
    value = input()
    config['setting'][setting] = value
    with open('settings.ini', 'w') as configfile:
        config.write(configfile)
def settingec():
    if 'setting' == cmd:
        settinge()
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
    langdetectcheck()
    shadowevalc()
    blacklistwhelpc()
    webblacklistdownloaderc()
    discordrpcoc()
    textwidget()
    blacklistwopenc()
    serverversionc()