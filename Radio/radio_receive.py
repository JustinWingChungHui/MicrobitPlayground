import radio
import speech
import music
from microbit import *

radio.on()

while True:
    try:
        incoming = radio.receive()
        #display.scroll(incoming,wait=False)
        #music.pitch(int(incoming))
        speech.say(incoming)
    except:
        pass
        