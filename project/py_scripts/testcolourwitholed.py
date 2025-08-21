from PiicoDev_Unified import sleep_ms
from colour import Colour
from OLED import OLED
screen = OLED(debug=False)
colours = Colour(debug = False)
while True:
    screen.show_state("NOTGREEN")
    sleep_ms(100)
    if colours.isgreen():
        screen.show_state("green")
        sleep_ms(200)