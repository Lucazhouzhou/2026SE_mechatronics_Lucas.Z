from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_Unified import sleep_ms
colourSensor = PiicoDev_VEML6040()
class Colour:
    def __init__(self,debug):
        self.__debug = debug
        self.__colour= colourSensor.readHSV()
    
    def gethue(self):
        colour = colourSensor.readHSV()
        hue = colour['hue']
        if self.__debug :
            print(f"hue is {hue}")
        return hue
    
    def isgreen(self):
        colour = colourSensor.readHSV()
        hue = colour['hue']
        if hue > 60 and hue < 160 :
            return True
        else :
            return False