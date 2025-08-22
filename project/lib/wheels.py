from machine import Pin,PWM
from servo import Servo
class Wheels: 
    def __init__(self,pin_L,pin_R,debug):
        self.wheels_state = "still"
        self.__debug=debug
        self.left_servo= Servo(PWM(Pin(pin_L)))
        self.rigth_servo = Servo(PWM(Pin(pin_R)))
    
    def forwardfast(self):
        if self.__debug :
            print("Going forward fast")
        self.left_servo.set_duty(500)
        self.rigth_servo.set_duty(2500)
        self.wheels_state = "forward fast"
    
    def forwardslow(self):
        if self.__debug :
            print("Going forward slow")
        self.left_servo.set_duty(1000)
        self.rigth_servo.set_duty(2000)
        self.wheels_state = "forward slow"

    def backwardfast(self):
        if self.__debug :
            print("Going backward fast")
        self.left_servo.set_duty(2500)
        self.rigth_servo.set_duty(500)
        self.wheels_state = "backward fast"

    def backwardslow(self):
        if self.__debug :
            print("Going backward slow")
        self.left_servo.set_duty(2000)
        self.rigth_servo.set_duty(1000)
        self.wheels_state = "backward slow"

    def turnleft(self):
        if self.__debug :
            print("Turning right")
        self.left_servo.set_duty(1000)
        self.rigth_servo.set_duty(1000)
        self.wheels_state = "Turn right"

    def turnright(self):
        if self.__debug :
            print("Turning left")
        self.left_servo.set_duty(2000)
        self.rigth_servo.set_duty(2000)
        self.wheels_state = "Turn left"

    def away(self):
        if self.__debug :
            print("towards")
        self.left_servo.set_duty(1250)
        self.rigth_servo.set_duty(2500)
        self.wheels_state = "towards"

    def towards(self):
        if self.__debug :
            print("away")
        self.left_servo.set_duty(500)
        self.rigth_servo.set_duty(1750)
        self.wheels_state = "away"

    def stop(self):
        if self.__debug:
            print("stop")
        self.left_servo.stop()
        self.rigth_servo.stop()