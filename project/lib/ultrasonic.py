from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms

class Ultrasonic:
    def __init__(self, debug=False):
        self.__debug = debug
        self.__front = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
        self.__side = PiicoDev_Ultrasonic(id=[0, 0, 0, 1])

    def getfrontdistance(self):
        distance = self.__front.distance_mm
        if self.__debug:
            print(f"Front distance: {distance} mm")
        return distance

    def getsidedistance(self):
        distance = self.__side.distance_mm
        if self.__debug:
            print(f"Side distance: {distance} mm")
        return distance

    def wallincoming(self, threshold):
        distance = self.getfrontdistance()
        if distance is not None and distance < threshold:
            if self.__debug:
                print(f"Wall detected at {distance} mm (threshold: {threshold} mm)")
            return True
        return False
    
    def rightsidehaswall(self):
        sidedistance = self.getsidedistance()
        if sidedistance is not None and sidedistance < 45:
            if self.__debug:
                print(f"Wall detected at {sidedistance} mm (threshold: 44 mm)")
            return True
        return False