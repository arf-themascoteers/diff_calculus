import matplotlib.pyplot as plt
import numpy as np

START = 0
END = 10
STEP = 100

x = np.linspace(START,END,STEP)
y = x**2

plt.plot(x,y)
plt.show()

dx = (END-START) / STEP
new_x = np.zeros_like(x)
new_y = np.zeros_like(x)
new_x[0] = 0
new_y[0] = 0
new_x[1] = 0 + dx
new_y[1] = (new_x[1])**2



current_x_point = new_x[1]
current_index = 2
dydx = 2 * current_x_point

while current_index < new_x.shape[0]:
    dy = dydx * dx
    current_x_point = current_x_point + dx
    previous_y_point = new_y[current_index - 1]
    current_y_point = previous_y_point + dy
    new_x[current_index] = current_x_point
    new_y[current_index] = current_y_point

    current_index = current_index + 1
    dydx = 2 * current_x_point

plt.plot(new_x, new_y)
plt.show()
exit(0)