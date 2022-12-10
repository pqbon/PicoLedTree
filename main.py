from tree_blink import tree_blink
from tree_led_sin import tree_led_sin
from tree_led_tan import tree_led_tan
from tree_pulse import tree_pulse
from tree_random import tree_led_rand
from tree_sin import tree_sin
import random

if __name__ == '__main__':
    while True :
        run_len = random.choice(range(100, 10000))
        tree_blink(run_len)
        run_len = random.choice(range(100, 10000))
        tree_led_sin(run_len)
        run_len = random.choice(range(100, 10000))
        tree_led_tan(run_len)
        run_len = random.choice(range(100, 10000))
        tree_pulse(run_len)
        run_len = random.choice(range(100, 10000))
        tree_led_rand(run_len)
        run_len = random.choice(range(100, 10000))
        tree_sin(run_len)
