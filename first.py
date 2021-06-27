import matplotlib.pyplot as plt
import numpy as np

START = 0
END = 9
SIZE = 100

x = np.linspace(START,END,SIZE)
y = x**2

dy = np.zeros_like(x)
dydx = np.zeros_like(x)

current_x_point = x[0]
current_index = 1

dx = (END-START) / SIZE

for current_index in range(SIZE-1):
    next_index = current_index + 1
    dy[current_index] = y[next_index] - y[current_index]
    dydx[current_index] = dy[current_index]/dx

x = x[1:-1]
dydx = dydx[1:-1]

plt.plot(x, dydx/x)
plt.show()

