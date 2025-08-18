import time
from wheels import Wheels
from PiicoDev_Unified import sleep_ms

car = Wheels(18,20,debug=True)

car.turnright()
sleep_ms(519)
car.stop()
