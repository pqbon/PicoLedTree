import time
import math
from pihubtree import PiHutTree 

def tree_led_tan(count):
    tree = PiHutTree()
    # Fade the LED in and out a few times.
    step_size = 360 / tree.length

    for idx in range(0, count):
        for jdx in range(tree.length): 
            deg = (idx + jdx) % tree.length
            bright = (math.tan(step_size * deg) + 1.0) * 0.5
            tree.set_led(jdx,bright)
        bright = (math.sin(idx) + 1.0) * 0.5
        tree.star = bright
        time.sleep(0.3)

if __name__ == '__main__':
    tree_led_tan(1000)