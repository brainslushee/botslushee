import string
import urllib2
import json

def getUser(line):
    separate = line.split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user
def getMessage(line):
    separate = line.split(":", 2)
    message = separate[2]
    return message
def getStreamer(line):
    separate = line.split(":", 2)
    message = separate[2]
    streamerSplit = message.split(" ", 2)
    if len(streamerSplit) == 2:
        streamer = streamerSplit[1]
        return streamer
def getStreamerInfo(line):
    separate = line.split(":", 2)
    message = separate[2]
    streamerSplit = message.split(" ", 2)
    if len(streamerSplit) == 2:
        streamer = streamerSplit[1]
        streamerurl = "https://api.twitch.tv/kraken/channels/" + streamer
        response = urllib2.urlopen(streamerurl)
        data = json.load(response)
        game = data["game"]
        return game
