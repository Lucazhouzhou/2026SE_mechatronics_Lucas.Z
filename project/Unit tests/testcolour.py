from PiicoDev_Unified import sleep_ms
from colour import Colour

colours = Colour(debug = True)
while True:
    colours.gethue()
    sleep_ms(100)
    if colours.isgreen():
        print("green")