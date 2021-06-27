import matplotlib.pyplot as plt
import numpy as np


START = 0
END = 9
SIZE = 100

x = np.linspace(START,END,SIZE)
y = x**2

dy = np.zeros_like(x)
dydx = np.zeros_like(x)
d2y_dx2 = np.zeros_like(x)
distance_dydx = np.zeros_like(x)

current_x_point = x[0]
current_index = 1

dx = (END-START) / SIZE

for current_index in range(SIZE-1):
    next_index = current_index + 1
    dy[current_index] = y[next_index] - y[current_index]
    dydx[current_index] = dy[current_index]/dx

for current_index in range(SIZE-2):
    next_index = current_index + 1
    distance_dydx[current_index] = dydx[next_index] - dydx[current_index]
    d2y_dx2[current_index] = distance_dydx[current_index]/dx


x = x[1:-2]
d2y_dx2 = d2y_dx2[1:-2]
d2y_dx2 = np.round(d2y_dx2,5)
plt.plot(x, d2y_dx2)

print(d2y_dx2)