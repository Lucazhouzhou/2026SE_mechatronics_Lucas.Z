from PiicoDev_Unified import sleep_ms
from colour import Colour

colours = Colour(debug = False)
while True:
    print(colours.gethue)
    sleep_ms(100)
    if colours.isgreeen():
        print("green")