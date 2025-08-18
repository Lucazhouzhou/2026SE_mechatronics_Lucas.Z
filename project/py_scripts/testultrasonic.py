from PiicoDev_Unified import sleep_ms
from ultrasonic import Ultrasonic
from wheels import Wheels
sonic = Ultrasonic(debug=True)
car = Wheels(18,20,debug=True)
while True :
    print(sonic.wallincoming(45))
    sleep_ms(100)
    car.forwardslow()
    if sonic.wallincoming(45):
        car.stop()
        sleep_ms(1000)