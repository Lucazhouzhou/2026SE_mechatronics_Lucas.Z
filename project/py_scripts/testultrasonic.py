from PiicoDev_Unified import sleep_ms
from ultrasonic import Ultrasonic
from wheels import Wheels
sonic = Ultrasonic(debug=True)
car = Wheels(18,20,debug=True)
while True :
    sonic.getsidedistance()
    sleep_ms(1000)
    sonic.getfrontdistance()
    sleep_ms(1000)
    sonic.rightsidehaswall()
    sleep_ms(1000)
    sonic.wallincoming(100)
    sleep_ms(1000)