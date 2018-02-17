import ZeroBorg
from time import sleep
#ZeroBorg.ScanForZeroBorg()

ZB = ZeroBorg.ZeroBorg()
ZB.i2cAddress = 0x40
ZB.Init()
ZB.ResetEpo()

ZB.SetMotor1(50)
ZB.SetMotor3(50)
sleep(2)
ZB.MotorsOff()
