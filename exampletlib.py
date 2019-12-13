import tlib
import time as ti

# Window (with name)
window = tlib.DefaultWindow('Example')

# Creating a GameObject (color, speed, coords, pixel size, shape)
example = tlib.GameObject('#21a6f6', 10, -100, 0, 40, 40, 'square')
example2 = tlib.GameObject('#dd2323', 10, 100, 0, 40, 40, 'circle')

# Movement binds on a window, with keybinds as up-down-left-right
example.simple_binds(['w', 's', 'a', 'd'], window)
example2.simple_binds(['h','k','j','l'], window)

while True:
	window.run()

window.screen.mainloop()