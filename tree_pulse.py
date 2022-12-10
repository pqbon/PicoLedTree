import time
from pihubtree import PiHutTree 

def tree_pulse(count):
    tree = PiHutTree()
    # Fade the LED in and out a few times.
    duty = 0.0
    direction = 2048
    for x in range(0, count):
        duty += direction
        if duty > 100:
            duty = 100.0
            direction = -2.0
        elif duty < 0:
            duty = 0.0
            direction = 2.0
        tree.brightness = (duty/100)
        time.sleep(0.025)

if __name__ == '__main__':
    tree_pulse(1000)