import matplotlib.pyplot as plt
import numpy as np

   
x = np.linspace(-2, 2, 100)

# calculate the y value for each element of the x vector
y = x**2

fig, ax = plt.subplots()
ax.plot(x, y)

plt.show()