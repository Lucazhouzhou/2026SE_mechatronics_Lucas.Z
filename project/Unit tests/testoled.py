from PiicoDev_Unified import sleep_ms
from OLED import OLED

oled = OLED(debug=True)

states = ["Idle", "Moving", "Stopped", "Error"]

for state in states:
    oled.show_state(state)
    sleep_ms(1000)
    oled.clear()
    sleep_ms(1000)