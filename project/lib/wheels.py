from machine import Pin
from time import sleep, time
class Wheels: 
    def __init__(self,pin_L,pin_R,debug):
        super().__init__(pin,Pin.OUT)
        self.wheels_state
        self.__debug=debug
        self.__pin_L= pin_L
        self.__pin_R = pin_R
    
    def forward(self):
        self.__pin_L.set_duty
        if self.__debug :
            print("Going forward")