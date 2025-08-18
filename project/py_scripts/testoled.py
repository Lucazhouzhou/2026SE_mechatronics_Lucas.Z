from OLED import OLED

screen = OLED(debug=True)
screen.show_state("RUN")
sleep_ms(2000)
screen.clear()