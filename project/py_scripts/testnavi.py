from PiicoDev_Unified import sleep_ms
from wheels import Wheels
from ultrasonic import Ultrasonic
from colour import Colour
from navigator import Navigator
colours = Colour(debug=False)
sonic = Ultrasonic(debug=False)
car = Wheels(18, 20, debug=False)
nav = Navigator(isgreen=colours.isgreen,
wallincoming=lambda:sonic.wallincoming(44),
rightsidehaswall=sonic.rightsidehaswall,
forwardfast=car.forwardfast,
forwardslow=car.forwardslow,
turnright=car.turnright,
turnleft=car.turnleft,
stop=car.stop, debug=True
)
sleep_ms(1000)
nav.controller()