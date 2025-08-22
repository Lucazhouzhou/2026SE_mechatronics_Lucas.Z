from wheels import Wheels
from PiicoDev_Unified import sleep_ms
wheels = Wheels(18, 20, True)
wheels.turnleft()
print(wheels.wheels_state)
sleep_ms(500)
wheels.stop()