from approxeng.input.selectbinder import ControllerResource
from approxeng.input.dualshock3 import DualShock3

from time import sleep



while True:
    try:
        # Get a joystick
        with ControllerResource(controller_class = DualShock3) as joystick:
            print('found and connected')

            
            while joystick.connected:   #loop for joystick
                presses = joystick.check_presses()
                if presses['square']:
                    print("Square pressed")
                
                
        print("Connection lost")
    except IOError:
        print("No joystick found")
        sleep(1)
