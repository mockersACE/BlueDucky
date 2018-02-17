import ZeroBorg3 as ZeroBorg
from time import sleep


ZB = ZeroBorg.ZeroBorg()

ZB.Init()
print("init")
ZB.ResetEpo()

print("here")

ZB.SetMotor1(50)
ZB.SetMotor3(50)
sleep(2)
ZB.MotorsOff()
