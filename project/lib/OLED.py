from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms

class OLED:
    def __init__(self, debug=False):
        self._debug = debug
        self._display = create_PiicoDev_SSD1306()
        if self._debug:
            print("[OLED] Display initialized")

    def clear(self):
        self._display.fill(0)
        self._display.show()
        if self._debug:
            print("[OLED] Display cleared")

    def show_state(self, state, x=30, y=20, size=1):
        self._display.fill(0)
        self._display.text(str(state), x, y, size)
        self._display.show()
        if self._debug:
            print(f"[OLED] Displayed state: '{state}' at ({x},{y}) size={size}")