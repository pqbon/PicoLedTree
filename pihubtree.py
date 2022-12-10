import time
from machine import Pin, PWM

class PiHutTree:
#Star = GPIO 2
#Tree Lights = GPIO 4, 15, 13, 21, 25, 8, 5, 10, 16, 17, 27, 26, 24, 9, 12, 6, 20, 19, 14, 18, 11, 7, 23 and 22.
    def __init__(self):
        self.STAR_PIN = 2
        self.LIGHT_PINS = [4, 15, 13, 21, 25, 8, 5, 10, 16, 17, 27, 26, 24, 9, 12, 6, 20, 19, 14, 18, 11, 7, 23, 22]
        self.PIN_MAP = {
            2: 2,
            3: 3,
            4: 14,
            17: 17,
            27: 27,
            22: 22,
            10: 11,
            9: 12,
            11: 10,
            5: 15,
            6: 6,
            13: 13,
            19: 19,
            26: 26,
            14: 4,
            15: 5,
            18: 18,
            23: 0, #23,
            24: 1, #24,
            25: 28,
            8: 8,
            7: 7,
            1: 1,
            12: 9,
            16: 16,
            20: 20,
            21: 21,
        }
        self.star_led = PWM(Pin(self.PIN_MAP[self.STAR_PIN], Pin.OUT))
        self.star_led.freq(1000)
        self.tree_leds = []
        for pin in self.LIGHT_PINS:
            pwm = PWM(Pin(self.PIN_MAP[pin], Pin.OUT))
            pwm.freq(100)
            self.tree_leds.append(pwm)
        self.star_b = 0
        self.led_b = []
        for pin in self.LIGHT_PINS:
            self.led_b.append(0)

    @property
    def length(self):
        return len(self.tree_leds)

    @property
    def brightness(self):
        return self.led_b[0]

    @brightness.setter
    def brightness(self, brightf):
        bright = int(65535 * brightf)
        #print("brightf: ", brightf, " bright: ", bright)
        self.star_led.duty_u16(bright)
        for light in self.tree_leds:
            light.duty_u16(bright)
    @property
    def star(self):
        return self.star_b

    @star.setter
    def star(self, brightf):
        bright = int(65535 * brightf)
        #print("star brightf: ", brightf, " bright: ", bright)
        self.star_led.duty_u16(bright)

    def set_led(self, idx, brightf):
        bright = int(65535 * brightf)
        #print(idx, " brightf: ", brightf, " bright: ", bright)
        self.tree_leds[idx].duty_u16(bright)
