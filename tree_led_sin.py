import time
import math
from pihubtree import PiHutTree 

def tree_led_sin(count):
    tree = PiHutTree()
    # Fade the LED in and out a few times.
    step_size = 360 / tree.length

    for idx in range(0, count):
        for jdx in range(tree.length): 
            deg = (idx + jdx) % tree.length
            bright = (math.sin(step_size * deg) + 1.0) * 0.5
            tree.set_led(jdx,bright)
        bright = (math.cos(idx) + 1.0) * 0.5
        tree.star = bright
        time.sleep(0.3)

if __name__ == '__main__':
    tree_led_sin(1000)