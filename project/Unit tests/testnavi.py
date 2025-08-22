from PiicoDev_Unified import sleep_ms
from wheels import Wheels
from ultrasonic import Ultrasonic
from colour import Colour
from navigator import Navigator
from OLED import OLED
colours = Colour(debug=False)
sonic = Ultrasonic(debug=False)
car = Wheels(18, 20, debug=False)
oled = OLED(debug=True)
nav = Navigator(isgreen=colours.isgreen,
wallincoming=lambda:sonic.wallincoming(150),
rightsidehaswall=sonic.rightsidehaswall,
forwardfast=car.forwardfast,
forwardslow=car.forwardslow,
turnright=car.turnright,
turnleft=car.turnleft,
show_state=oled.show_state,
clear=oled.clear,
stop=car.stop, debug=True
)
sleep_ms(1000)
nav.controller()