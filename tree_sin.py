import time
import math
from pihubtree import PiHutTree 

def tree_sin(count):
    tree = PiHutTree()
    # Fade the LED in and out a few times.
    for idx in range(0, count):
        bright = (math.sin(idx) + 1.0) * 0.5
        tree.brightness = bright
        time.sleep(0.05)

if __name__ == '__main__':
    tree_sin(1000)