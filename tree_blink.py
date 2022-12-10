import time
from pihubtree import PiHutTree 

def tree_blink(count):
    tree = PiHutTree()
    # Fade the LED in and out a few times.
    for _ in range(0, count):
        tree.brightness = 1.0
        time.sleep(0.666)
        tree.brightness = 0.0
        time.sleep(0.333)

if __name__ == '__main__':
    tree_blink(100)