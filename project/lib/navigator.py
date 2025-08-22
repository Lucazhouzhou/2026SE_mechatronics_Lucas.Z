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
            if not self.__wallincoming() and not self.__rightsidehaswall() :
                    self.__forwardslow()
                    sleep_ms(500)
                    self.state = "FACEDTURN"
                    self.__showstate(self.state)
                    self.__stop()
                    sleep_ms(200)
                    self.state = "TURNING right"
                    self.__showstate(self.state)
                    self.__turnright()
                    sleep_ms(440)
                    self.__stop()
                    self.__forwardslow()
                    sleep_ms(1500)
            elif self.__wallincoming() and self.__rightsidehaswall():
                    self.state = "TURNING LEFT"
                    self.__showstate(self.state)
                    self.__stop()
                    sleep_ms(200)
                    self.state = "TURNINGLEFT"
                    self.__showstate(self.state)
                    self.__turnleft()
                    sleep_ms(480)
                    self.__forwardslow()
                    sleep_ms(1000)
            else :
                self.__forwardfast()
                self.state = "IDLE"
                self.__showstate(self.state)
                sleep_ms(500)
