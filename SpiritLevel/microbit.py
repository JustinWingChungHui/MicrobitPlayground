# Add your Python code here. E.g.
from microbit import *

far_left = Image("90000:"
                "90000:"
                "90000:"
                "90000:"
                "90000")
                
left = Image("09000:"
                "09000:"
                "09000:"
                "09000:"
                "09000")
                
level = Image("00900:"
                "00900:"
                "00900:"
                "00900:"
                "00900")
                
far_right = Image("00009:"
                "00009:"
                "00009:"
                "00009:"
                "00009")
                
right = Image("00090:"
                "00090:"
                "00090:"
                "00090:"
                "00090")
while True:
    reading = accelerometer.get_x()
    if reading > 100:
        display.show(far_right)
    elif reading > 20:
        display.show(right)
    elif reading > -20:
        display.show(level)
    elif reading > -100:
        display.show(left)
    else:
        display.show(far_left)


    




