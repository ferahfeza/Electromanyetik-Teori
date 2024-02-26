import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos, pi, linspace

fig, ax = plt.subplots(figsize=(8, 8))
#draw point at orgin
#plt.plot(0,0, color = 'red', marker = 'o')
#plt.gca().annotate('O (0, 0)', xy=(0 + 0.1, 0 + 0.1), xycoords='data', fontsize=10)
#draw circle
r = 3
angles = linspace(0 * pi, 2 * pi, 100 )
xs = r * cos(angles)
ys = r * sin(angles)
plt.plot(xs, ys, color = 'green')
plt.grid()
#draw radius
#plt.plot(0, 0, marker = 'o', color = 'purple')
#plt.plot(1.5, 0, marker = 'o', color = 'purple')
plt.plot([0, 3], [0, 0], color = 'purple')
#plt.gca().annotate('Radius', xy=(0.5, -0.2), xycoords='data', fontsize=10)
#draw another radius
plt.plot([0,3.75],[0,0], color = 'blue')
plt.plot(r * cos(pi /4), r * sin( pi / 4), marker = 'o', color = 'orange')
plt.plot(r * cos(5*pi /4), r * sin( 5*pi / 4), marker = 'o', color = 'orange')
plt.plot([0, 1.25*r * cos(pi /4)], [0, 1.25*r * sin( pi / 4)], color = "purple")
plt.plot([0, 1.25*r * cos(5*pi /4)], [0, 1.25*r * sin( 5*pi / 4)], color = "purple")
plt.arrow(0,0,3.75,0,width=0.025)
plt.arrow(0,0,0,3.75,width=0.025)
plt.arrow(0,0,2.9*cos(3*pi/4),2.9*sin(3*pi/4),width=0.02)
plt.annotate('$x$',xy=(3.95,0),xytext=(3.85,0),size=14)
plt.annotate('$y$',xy=(0,3.95),xytext=(0,3.95),size=14)
plt.annotate('$q_1$',xy=(-2,-2.2),xytext=(-2,-2.2),size=14)
plt.annotate('$q_2$',xy=(2.3,2),xytext=(2.3,2),size=14)
plt.annotate('$a$',xy=(-1,1),xytext=(-1,1),size=14)
plt.annotate('$y=x$',xy=(2.8,2.8),xytext=(2.8,2.8),size=14, color="purple")
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.gca().set_aspect('equal')

plt.show()