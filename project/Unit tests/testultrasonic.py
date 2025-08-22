from ultrasonicsensor import Ultrasonic
ultra = Ultrasonic(debug=True)

threshold = 100

while True:
    front = ultra.getfrontdistance()
    side = ultra.getsidedistance()
    
    print(f"Front distance: {front} mm")
    print(f"Side distance: {side} mm")
    
    if ultra.wallincoming(threshold):
        print(f"Front wall detected at {front} mm")
    
    if ultra.rightsidehaswall():
        print(f"Right-side wall detected at {side} mm")
    
    sleep_ms(500)