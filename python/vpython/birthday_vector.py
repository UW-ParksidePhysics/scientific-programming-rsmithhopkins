from vpython import *
# GlowScript 3.0 VPython

# Written by Ruth Chabay, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

from vpython import scene, cylinder, label, arrow, vector, color  # Import necessary VPython modules

scene.background = color.white
scene.width = 600
scene.height = 600
scene.forward = vector(-0.5, -0.3, -1)

scene.caption = """To rotate 'camera', drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

# Draw axes
x_axis = cylinder(color=vector(1, 0, 0), pos=vector(0, 0, 0), axis=vector(10, 0, 0), radius=0.3)
x_label = label(pos=vector(11, 0, 0), text="x", color=color.red, opacity=0, height=30, box=False)

y_axis = cylinder(color=vector(0, 1, 0), pos=vector(0, 0, 0), axis=vector(0, 10, 0), radius=0.3)
y_label = label(pos=vector(0, 11, 0), text="y", color=color.green, opacity=0, height=30, box=False)

z_axis = cylinder(color=vector(0, 0, 1), pos=vector(0, 0, 0), axis=vector(0, 0, 10), radius=0.3)
z_label = label(pos=vector(0, 0, 11), text="z", color=color.blue, opacity=0, height=30, box=False)

# Create a vector in the first octant
# Numbers come from birth dates and their months: 7 (July), 12 (December), and 9 (September)
custom_vector = arrow(pos=vector(0, 0, 0), axis=vector(7, 12, 9), color=color.orange, shaftwidth=0.5)

# Label the vector as r = ax + by + cz
vector_label = label(pos=vector(8, 13, 10), text="r = 7x + 12y + 9z", color=color.orange, height=20, box=False)
