import tlib
import time as ti

# Window (with name)
window = tlib.DefaultWindow('Example')

# Creating a GameObject (color, speed, coords, pixel size, shape)
example = tlib.GameObject('#21a6f6', 10, -100, 0, 40, 40, 'square')
example2 = tlib.GameObject('#dd2323', 10, 100, 0, 40, 40, 'circle')
example3 = tlib.StaticBox('#194572', 20, 200, 60, 20)

# Movement binds on a window, with keybinds as up-down-left-right
example.simple_binds(['w', 's', 'a', 'd'], window)

# These are more keybinds
example2.simple_binds(['u','j','h','k'], window)

# This probably could be shortened, but not now.
window.run()

ti.sleep(1)
example3.align_left(0)

# Will clean this kind of loop up later.
while True:
	window.run()
	example.move(example.unit_vec(example2))
	ti.sleep(0.05)