import string
import pyautogui
import time
import urllib2

from Read import getUser, getMessage, getStreamer, getStreamerInfo
from Socket import openSocket, sendMessage
from Initialize import joinRoom

s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
    if "PING" in s.recv(1024):
        s.send.replace("PING", "PONG")
        time.sleep(1)

while True:
    readbuffer = readbuffer + s.recv(1024)
    temp = string.split(readbuffer, "\n")
    readbuffer = temp.pop()


    for line in temp:

        #PING function goes here

        user = getUser(line)
        message = getMessage(line)
        streamer = getStreamer(line)
        game = getStreamerInfo(line)

        print user + " typed: " + message

        #Botslushee Commands

        #Brainscan
        if message.startswith("!brainscan"):
            sendMessage(s, "Sorry, !brainscan is temporarily unavailable.")
        #Shows last game streamer played and links channel ERROR HERE
        if message.startswith("!streamer "):
            sendMessage(s, "Follow " + streamer + " at twitch.tv/" + streamer +
            "! They last played: " + game + "!")
        #Activates the webcam in OBS for 5 seconds - Coordinates may vary
        if message.startswith("!reaction"):
            pyautogui.click(832,896)
            time.sleep(5)
            pyautogui.click(832,896)
