
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms
from colour import Colour
from wheels import Wheels
from OLED import OLED

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

class Navigator():
    def __init__(self, forwardfast, forwardslow, turnright, turnleft, stop,
                wallincoming, rightsidehaswall, isgreen, show_state, clear, debug):
        self.__forwardfast = forwardfast
        self.__forwardslow = forwardslow
        self.__turnright = turnright
        self.__turnleft = turnleft
        self.__stop = stop
        self.__wallincoming = wallincoming
        self.__rightsidehaswall = rightsidehaswall
        self.__isgreen = isgreen
        self.__debug = debug
        self.__showstate = show_state
        self.__clear = clear
        self.state = "IDLE"

    def controller(self):
        while True:
            self.__showstate(self.state)

            front_distance = getfrontdistance(debug=True)
            side_distance = getsidedistance(debug=True)

            front_wall = front_distance is not None and front_distance < 150
            side_wall = side_distance is not None and side_distance < 132

            print(f"Wallincoming check: {front_wall} | Distance: {front_distance} mm")
            print(f"Side wall check: {side_wall} | Distance: {side_distance} mm")
