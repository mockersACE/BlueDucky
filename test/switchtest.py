from gpiozero import Button
from time import sleep

KILL = Button(23)

while True:
    if KILL.is_pressed == True:
        print('true')
    if KILL.is_pressed == False:
        print('false')
    sleep(1)
