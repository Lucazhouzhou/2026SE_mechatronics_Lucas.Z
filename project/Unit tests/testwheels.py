from wheels import Wheels
from PiicoDev_Unified import sleep_ms
wheels = Wheels(18, 20, True)

    wheels.forwardfast()
    print(wheels.wheels_state)
    sleep_ms(1000)
    
    wheels.forwardslow()
    print(wheels.wheels_state)
    sleep_ms(1000)
    
    wheels.backwardfast()
    print(wheels.wheels_state)
    sleep_ms(1000)
    
    wheels.backwardslow()
    print(wheels.wheels_state)
    sleep_ms(1000)
    
    wheels.turnleft()
    print(wheels.wheels_state)
    sleep_ms(1000)
    
    wheels.turnright()
    print(wheels.wheels_state)
    sleep_ms(1000)
    
    wheels.away()
    print(wheels.wheels_state)
    sleep_ms(1000)
    
    wheels.towards()
    print(wheels.wheels_state)
    sleep_ms(1000)
    
    wheels.stop()
    print(wheels.wheels_state)
    sleep_ms(1000)
