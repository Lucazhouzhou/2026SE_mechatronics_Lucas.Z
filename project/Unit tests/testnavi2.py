from PiicoDev_Unified import sleep_ms
from wheels import Wheels
from colour import Colour
from navigator2 import Navigator
from OLED import OLED
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic

colours = Colour(debug=False)
car = Wheels(18, 20, debug=False)
oled = OLED(debug=True)

front_sensor = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
side_sensor = PiicoDev_Ultrasonic(id=[0, 0, 0, 1])

def getfrontdistance(debug=False):
    distance = front_sensor.distance_mm
    if debug:
        print(f"[getfrontdistance] Distance: {distance}")
    return distance

def getsidedistance(debug=False):
    distance = side_sensor.distance_mm
    if debug:
        print(f"Side distance: {distance} mm")
    return distance

def wallincoming(threshold=150, debug=False):
    distance = getfrontdistance(debug)
    if distance is not None and distance < threshold:
        if debug:
            print(f"Wall detected at {distance} mm (threshold: {threshold} mm)")
        return True
    return False

def rightsidehaswall(debug=False):
    sidedistance = getsidedistance(debug)
    if sidedistance is not None and sidedistance < 132:
        if debug:
            print(f"Wall detected at {sidedistance} mm (threshold: 150 mm)")
        return True
    return False

nav = Navigator(
    isgreen=colours.isgreen,
    wallincoming=lambda debug: wallincoming(debug),
    rightsidehaswall=lambda debug: rightsidehaswall(debug),
    forwardfast=car.forwardfast,
    forwardslow=car.forwardslow,
    turnright=car.turnright,
    turnleft=car.turnleft,
    show_state=oled.show_state,
    clear=oled.clear,
    stop=car.stop,
    debug=True
)


sleep_ms(1000)
nav.controller()