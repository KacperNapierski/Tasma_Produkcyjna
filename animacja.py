import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.animation import FuncAnimation
import time

fig, ax = plt.subplots()


# kształty
ax.set(xlim=(-1, 11), ylim=(-1, 2))

circle_a = plt.Circle((0, 0), 0.5, fc="gray")
ax.add_artist(circle_a)
circle_b = plt.Circle((10, 0), 0.5, fc="gray")
ax.add_artist(circle_b)

line_a = plt.Line2D((0, 10), (0.5, 0.5), 1, "-", "brown")
ax.add_artist(line_a)
line_b = plt.Line2D((0, 10), (-0.5, -0.5), 1, "-", "brown")
ax.add_artist(line_b)

rectangle = plt.Rectangle((0, 2), 0.5, 0.75, fc="r")


#funkcje
def init():
    ax.add_artist(rectangle)
    rectangle.set_xy((0,2))
    return rectangle,



def animate_y(i):
    if i < 150: 
        rectangle.set_y(-i*0.01+2)
    if i >=150:
        print(i)
        i=i%150
        print(i)
        rectangle.set_x(i*0.06)
    return rectangle,

#animacja
anim1=animation.FuncAnimation(fig, animate_y, 
            init_func=init, frames=300, interval=10,
            blit=True,repeat=True)
plt.show()