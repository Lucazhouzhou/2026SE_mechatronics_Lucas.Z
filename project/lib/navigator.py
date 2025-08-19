from PiicoDev_Unified import sleep_ms
from colour import Colour
from ultrasonic import Ultrasonic
from wheels import Wheels
from OLED import OLED

class Navigator():
    def __init__(self,forwardfast,forwardslow,turnright,turnleft,stop,wallincoming,rightsidehaswall,isgreen,show_state,clear,debug):
        self.__forwardfast = forwardfast
        self.__forwardslow = forwardslow
        self.__turnright  = turnright
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
            if self.__isgreen():
                self.state = "GREEN"
                self.__showstate(self.state)
                self.__stop()
                sleep_ms(500)
            if self.__wallincoming():
                    self.state = "FACEDWALL"
                    self.__showstate(self.state)
                    self.__stop()
                    sleep_ms(200)
                    self.__turnleft()
                    sleep_ms(519)
            elif not self.__wallincoming() and not self.__rightsidehaswall() :
                    self.__stop()
                    sleep_ms(200)
                    self.__turnright()
                    sleep_ms(519)
            else :
                self.__forwardfast()