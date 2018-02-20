#________________________________________________
#Info
#Left motor = motor 1, Right motor = motor 3, Gun = motor 2



#__________________________________________________________________________
#imports
import ZeroBorg3 as ZeroBorg #for zeroborg
from time import sleep
from evdev import InputDevice, categorize, ecodes #for controller

#screen specific imports
from lib_oled96 import ssd1306
from smbus import SMBus
from PIL import ImageFont, ImageDraw, Image

#setup screen
i2cbus = SMBus(1)     
oled = ssd1306(i2cbus)
draw = oled.canvas
font = ImageFont.truetype('FreeSans.ttf', 20) #set font

#kill switch import
from gpiozero import Button

#setup kill switch
KILL = Button(23)

#check kill switch is raised
while KILL.is_pressed == False:
    draw.text((0, 0), 'Raise kill', font=font, fill=1) #line 1
    draw.text((0, 20), 'switch', font=font, fill=1) #line 2
    oled.display()
    sleep(1)

oled.cls() 
    

#ask for controller to be connected
draw.text((0, 0), 'Waiting for', font=font, fill=1) #line 1
draw.text((0, 20), 'controller...', font=font, fill=1) #line 2
draw.text((0, 40), '10', font=font, fill=1) #line 3
oled.display()

COUNT = 10 #seconds to wait

for x in range (0,10):
    oled.cls() 
    COUNTSTR = str(COUNT)
    draw.text((0, 0), 'Waiting for', font=font, fill=1) #line 1
    draw.text((0, 20), 'controller...', font=font, fill=1) #line 2
    draw.text((0, 40), COUNTSTR, font=font, fill=1) #line 3
    oled.display()
    sleep(1)
    COUNT = COUNT - 1

oled.cls() #clears oled

#PS3 setup
PS3 = InputDevice('/dev/input/event3')
draw.text((0, 0), 'Controller', font=font, fill=1) #line 1
draw.text((0, 20), 'connected', font=font, fill=1) #line 2
oled.display()
sleep(2)
oled.cls() 
    
#Zeroborg setup
ZB = ZeroBorg.ZeroBorg()
ZB.Init()
print("init")
ZB.ResetEpo()

#make font small
font = ImageFont.truetype('FreeSans.ttf', 10) #set font

#_____________________________________________________________________________
#Setup functions

def remotecontrol():
    oled.cls()
    draw.text((0, 0), 'Remote Control', font=font, fill=1) #line 1
    oled.display()
    while KILL.is_pressed == True:
        draw.text((0, 11), 'Drop kill switch', font=font, fill=1) #line 2
        oled.display()

    oled.cls()
    draw.text((0, 0), 'Remote Control', font=font, fill=1) #line 1
    draw.text((0, 11), 'Kill switch armed', font=font, fill=1) #line 2
    oled.display()
    
    while KILL.is_pressed == False:
        for event in PS3.read_loop():
            if event.type == ecodes.EV_KEY:
                if event.code == 292 and event.value == 1: #up button pressed
                    ZB.SetMotor1(70)
                    ZB.SetMotor3(70)
                if event.code == 294 and event.value == 1: #down button pressed
                    ZB.SetMotor1(-70)
                    ZB.SetMotor3(-70)
                if event.code == 293 and event.value == 1: #right button pressed
                    ZB.SetMotor1(70)
                    ZB.SetMotor3(-70)
                if event.code == 295 and event.value == 1: #left button pressed
                    ZB.SetMotor1(-70)
                    ZB.SetMotor3(70)
                if event.value == 0: #button released
                    ZB.SetMotor1(0)
                    ZB.SetMotor3(0)
                if KILL.is_pressed == True:
                    ZB.MotorsOff()
                    break
            if KILL.is_pressed == True:
                ZB.MotorsOff()
                break


    
    sleep(1)
    oled.cls() 

def straightline():
    oled.cls()
    draw.text((0, 0), 'Straight Line', font=font, fill=1) #line 1
    oled.display()
    sleep(1)
    oled.cls()

def maze():
    oled.cls()
    draw.text((0, 0), 'Maze', font=font, fill=1) #line 1
    oled.display()
    sleep(1)
    oled.cls()

def rainbow():
    oled.cls()
    draw.text((0, 0), 'Rainbow', font=font, fill=1) #line 1
    oled.display()
    sleep(1)
    oled.cls() 



#_____________________________________________________________________________
#Main menu and loop

MAINRUN = 1
while MAINRUN == 1:
    draw.text((0, 0), 'Main Menu', font=font, fill=1) #line 1
    draw.text((0, 11), 'X = Remote Control', font=font, fill=1) #line 2
    draw.text((0, 22), '[] = Straight Line', font=font, fill=1) #line 3
    draw.text((0, 33), '^ = Maze', font=font, fill=1) #line 4
    draw.text((0, 44), 'O = Rainbow', font=font, fill=1) #line 5
    oled.display()
    for event in PS3.read_loop():
        if event.type == ecodes.EV_KEY:
            if event.code == 302:
                remotecontrol()
                break
            if event.code == 303:
                straightline()
                break
            if event.code == 300:
                maze()
                break
            if event.code == 301:
                rainbow()
                break

