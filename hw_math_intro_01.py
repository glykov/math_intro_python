import numpy as np
import matplotlib.pyplot as plt
y = lambda k, x: np.cos(k * x)
fig = plt.subplots()
x = np.linspace(-10, 10, 100)
plt.plot(x, y(1, x))
plt.plot(x, y(3, x))
plt.show()
