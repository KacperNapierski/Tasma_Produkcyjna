import matplotlib.pyplot as plt
import matplotlib.animation as animation
#import animaplot as amp
import numpy as np
from matplotlib.animation import FuncAnimation
import time

fig, ax = plt.subplots()
fps = 30

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



def init():
    ax.add_artist(rectangle)
    rectangle.set_xy((0,2))
    return rectangle,

def animate_x(i):
    rectangle.set_x(i*0.01)
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

#def animate_y(i):
 #   if i < 150: 
  #      rectangle.set_y(-i*0.01+2)
  #  if i >=150:
   #     rectangle.set_x(i*0.01)


anim1=animation.FuncAnimation(fig, animate_y, 
            init_func=init, frames=300, interval=10,
            blit=True,repeat=True)
plt.show()
#anim1._stop()
#anim1.frame_seq.close()
#anim1.event_source.__closure__()

#plt.pause(0.5)


anim2=animation.FuncAnimation(fig, animate_x, init_func=init, 
            frames=1000, interval=10,blit=True) #10
plt.show()




#for j in range(1, 21):
    #for i in range(1, 31):
     #  rectangle.set_x(i*j*0.1)

# funkcje
# def animation_frame(i):
# x_data.append(i*10)
# y_data.append(i)
# return


# animacja
#animation = FuncAnimation(fig,)

      #  plt.show()
        #plt.pause(0.1)
        #plt.clf()
        #plt.draw(rectangle)
       # plt.close()
