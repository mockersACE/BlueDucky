from evdev import InputDevice, categorize, ecodes

PS3 = InputDevice('/dev/input/event3')

print(PS3)

for event in PS3.read_loop():
    if event.type == ecodes.EV_KEY:
        print(event.code)
