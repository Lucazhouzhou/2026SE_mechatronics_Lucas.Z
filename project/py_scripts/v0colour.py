from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_Unified import sleep_ms
colourSensor = PiicoDev_VEML6040()
while True:
    ### Example 1: Print Raw RGB Data
    data = colourSensor.readHSV() # Read the sensor (Colour space: Red Green Blue)
    hue = data['hue']
    if hue > 70 and hue < 80:
        print ("green")
        sleep_ms(100)
    else:
        print (hue)