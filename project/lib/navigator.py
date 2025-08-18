from PiicoDev_Unified import sleep_ms
from colour import Colour
from ultrasonic import Ultrasonic
from wheels import Wheels

class Navigator():
    def __init__(self,forwardfast,forwardslow,turnright,turnleft,stop,wallincoming,rightsidehaswall,isgreen,debug):
        self.__forwardfast = forwardfast
        self.__forwardslow = forwardslow
        self.__turnright  = turnright
        self.__turnleft = turnleft
        self.__stop = stop
        self.__wallincoming = wallincoming
        self.__rightsidehaswall = rightsidehaswall
        self.__isgreen = isgreen
        self.__debug = debug

    def controller(self):
        while True:
            if self.__wallincoming():
                    print(self.__wallincoming)
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