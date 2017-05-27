import radio
import speech
import music
from microbit import *

radio.on()

while True:
    if button_a.is_pressed():
        radio.send("button ay")
    if button_a.is_pressed():
        radio.send("button be")
   
    # stops multiple messages sent o one button press
    sleep(500)   