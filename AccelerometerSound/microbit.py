# Add your Python code here. E.g.
from microbit import *
import music

while True:
    reading = accelerometer.get_x()
    music.pitch(reading)


    




